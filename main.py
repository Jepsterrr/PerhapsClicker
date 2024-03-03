import pygame
from pygame.locals import *
import allSprites
import allUpgrades
import Values
import pygame.freetype
from random import uniform
# Importering av alla moduler som behövs och gjorts.
Original = 0
Help = 0

pygame.init()
pygame.display.set_caption('Energy Maker') # Vad pygame fönstret heter
logo = pygame.image.load('imagez/energy.png')
logo.set_colorkey((0,0,0)) # Så att svart försvinner från bilden
pygame.display.set_icon(logo) # Pygame fönstrets logga

autoEnergyEvent = pygame.USEREVENT + 1

def SpritePurchase(sprite): # Funktion vid köp av saker som ger energi
  if sprite.cost <= Values.energyNum: # Ifall man har tillräckligt
    Values.energyNum = Values.energyNum - sprite.cost # Tar bort så mycket den kostar
    sprite.cost = sprite.cost * uniform(1,1.15) # Sätter det nya värdet
    sprite.cost = round(sprite.cost, 1) # Avrundar
    sprite.amount += 1 # En till i antalet
    Values.autoEnergy += sprite.generate * sprite.upgrade * Values.EnergyMultiplier # Lägger till dess inkomst * dess uppgradering * en uppgradering man kan köpa, i automatiska

def SpriteUpgradePurchase(sprite, spriteUpgrade): # Funktion vid köp av saker som uppgraderar inkomsten av energi
  if spriteUpgrade.cost <= Values.energyNum:
    Values.energyNum = Values.energyNum - spriteUpgrade.cost # Bort med så mycket den kostar
    spriteUpgrade.cost = spriteUpgrade.cost * 3.5 # Nya kostnaden
    Values.autoEnergy -= sprite.generate * sprite.amount * sprite.upgrade * Values.EnergyMultiplier # Tar bort gamla värden
    sprite.upgrade *= 2 # 2x på dess uppgradering (1 från början)
    Values.autoEnergy += sprite.generate * sprite.amount * sprite.upgrade * Values.EnergyMultiplier # Nya automatiska inkomsten

def SpriteGoldenPurchase(goldenSprite): # Funktion vid köp av saker som uppgraderar allt
  if goldenSprite.cost <= Values.goldenEnergy:
    Values.goldenEnergy = Values.goldenEnergy - goldenSprite.cost # Bort med så mycket den kostar
    goldenSprite.cost = goldenSprite.cost * 3 # Nya kostnaden

# Vissa enkla sprites som defineras son inte har någon stor funktion i själva spelet
class ShopButton(pygame.sprite.Sprite):
  def __init__(self):
      pygame.sprite.Sprite.__init__(self)
      self.image = pygame.image.load('imagez/shopIcon.png').convert()
      self.image = pygame.transform.scale(self.image, (100,70))
      self.rect = self.image.get_rect()
      self.rect.x = Values.width/3 - 60
      self.rect.y = Values.height - 100

class BackButton(pygame.sprite.Sprite): # Samma princip som ovan
  def __init__(self):
      pygame.sprite.Sprite.__init__(self)
      self.image = pygame.image.load('imagez/backbutton.png').convert()
      self.image = pygame.transform.scale(self.image, (100,70))
      self.rect = self.image.get_rect()
      self.rect.x = Values.width/2 - 60
      self.rect.y = Values.height - 100

class ExclamationMark(pygame.sprite.Sprite):
  def __init__(self):
    pygame.sprite.Sprite.__init__(self)
    self.image = pygame.image.load('imagez/exclamationMark.png').convert()
    self.image = pygame.transform.scale(self.image,(25,25))
    self.image.convert_alpha()
    self.rect = self.image.get_rect()
    self.rect.x = Values.width /2 - 90
    self.rect.y = Values.height - 110

class StartArrow(pygame.sprite.Sprite):
  def __init__(self):
    pygame.sprite.Sprite.__init__(self)
    self.image = pygame.image.load('imagez/arrow.jpg').convert()
    self.image = pygame.transform.scale(self.image,(60,25))
    self.image.convert_alpha()
    self.rect = self.image.get_rect()
    self.rect.x = Values.width /2 - 50
    self.rect.y = Values.height /2 - 20

# Pygame group krävs till när jag ritar ut dem i spel-loopen
energy_list = pygame.sprite.Group() # En grupp för energi-ikonen som man klickar
energy_list.add(allSprites.energy) # Lägger till den spriten i gruppen

shopButton = ShopButton()
shopButton_list = pygame.sprite.Group()
shopButton_list.add(shopButton)

backButton = BackButton()
backButton_list = pygame.sprite.Group()
backButton_list.add(backButton)

exclamationMark = ExclamationMark()
exclamationMark_list = pygame.sprite.Group()
exclamationMark_list.add(exclamationMark)

startArrow = StartArrow()
startArrow_list = pygame.sprite.Group()
startArrow_list.add(startArrow)

evolution_list = pygame.sprite.Group()
evolution_list.add(allSprites.evolution)

goldenUpgrades_list = pygame.sprite.Group()
goldenUpgrades_list.add(allUpgrades.energy2x, allUpgrades.fasterEnergy, allUpgrades.upgrade50, allUpgrades.energy50)

incomes_list = pygame.sprite.Group()
incomes_list.add(allSprites.windmill, allSprites.electricWindmill, allSprites.solarpanel, allSprites.advancedSolar, allSprites.windpump, allSprites.oilRefinery, allSprites.recycling, allSprites.waterwheel, allSprites.bioplant, allSprites.gasFactory, allSprites.thermalGen, allSprites.oilRig, allSprites.coalFactory, allSprites.waterDam, allSprites.workers, allSprites.powerlines, allSprites.nuclear, allSprites.chemicals, allSprites.atoms, allSprites.world, allSprites.sun)

upgrades_list = pygame.sprite.Group()
upgrades_list.add(allUpgrades.clicker, allUpgrades.procentualEnergy, allUpgrades.windmillUpgrade, allUpgrades.electricWindmillUpgrade, allUpgrades.solarpanelUpgrade, allUpgrades.advancedSolarUpgrade, allUpgrades.windpumpUpgrade, allUpgrades.oilRefineryUpgrade, allUpgrades.recyclingUpgrade, allUpgrades.waterwheelUpgrade, allUpgrades.bioplantUpgrade, allUpgrades.gasFactoryUpgrade, allUpgrades.thermalGenUpgrade, allUpgrades.oilRigUpgrade, allUpgrades.coalFactoryUpgrade, allUpgrades.waterDamUpgrade, allUpgrades.workersUpgrade, allUpgrades.powerlinesUpgrade, allUpgrades.nuclearUpgrade, allUpgrades.chemicalsUpgrade, allUpgrades.atomsUpgrade, allUpgrades.worldUpgrade, allUpgrades.sunUpgrade)

pygame.time.set_timer(autoEnergyEvent, Values.autoEnergyTimer) # Man får energi var 1/10 sekund, i Energy.auto() så är den också /10 eftersom det ska bli lite mer estetiskt när man tjänar.

Game = True
while Game: # Spel-loopen
  Values.clock.tick(60) # FPS eller tick
  
  for event in pygame.event.get(): # Event är saker som sker medan loopen körs
    if event.type == pygame.QUIT: # Klickar ner spelet
        Game = False # Loop stoppas
        exit()
        pygame.quit()

    if event.type == autoEnergyEvent: # Egengjort event som är auto-energi
      allSprites.Energy.auto()
    
    if event.type == pygame.MOUSEBUTTONDOWN: # Ifall man vänsterklickar
      if Values.Shop is True: # Ifall man är i affärsmenyn
        if backButton.rect.collidepoint(pygame.mouse.get_pos()): # Om man trycker tillbaka
          Values.Shop = False # Inte längre i affärsmenyn
        
        if allUpgrades.clicker.rect.collidepoint(pygame.mouse.get_pos()): # Trycker på 2x på klicks
          if allUpgrades.clicker.cost <= Values.energyNum: # Tillräckligt med energi
            Values.energyNum = Values.energyNum - allUpgrades.clicker.cost # Bort med kostnaden
            allUpgrades.clicker.cost = allUpgrades.clicker.cost * 5 # Ny kostnad
            allUpgrades.clicker.upgrade *= 2 # 2x på klicks nu
            # SpritePurchase() Fungerar inte på denna eftersom det inte är någon auto med då det endast är när man klickar

        if allUpgrades.procentualEnergy.rect.collidepoint(pygame.mouse.get_pos()): # Samma princip som ovan eftersom det ger +0.05 istället för *2 + ingen self.upgrade
          if allUpgrades.procentualEnergy.cost <= Values.energyNum:
            Values.energyNum = Values.energyNum - allUpgrades.procentualEnergy.cost
            allUpgrades.procentualEnergy.cost = allUpgrades.procentualEnergy.cost * 2
            Original = Values.autoEnergy
            Values.autoEnergy -= Values.autoEnergy * Values.EnergyMultiplier
            Values.EnergyMultiplier += 0.05
            Values.autoEnergy += Original * Values.EnergyMultiplier
        
        for upgrade in upgrades_list: # Går igenom alla upgraderingar möjliga
          for i in range(len(allUpgrades.upgradeSpriteList)): # Går igenom varje siffra i längden av listan
            if upgrade.rect.collidepoint(pygame.mouse.get_pos()):
              if upgrade == allUpgrades.upgradeSpriteList[i]: # Ifall upgraderingen är samma sak som upgraderingen i listan
                SpriteUpgradePurchase(allSprites.spriteList[i], upgrade) # Eftersom sprite listan och upgraderings listan är i samma ordning kan man använda samma variabel -> i för att användas i funktionen

        for golden in goldenUpgrades_list: # Går igenom listan
          if golden.rect.collidepoint(pygame.mouse.get_pos()): # Om man klickar på någon av dessa uppgraderingar
            if golden == allUpgrades.energy2x: # Om det är just denna
              SpriteGoldenPurchase(golden) # Köp denna
              Values.energyX *= 2 # 2x på energi (används för klick)
              for incomes in incomes_list: # För varje sak i listan
                incomes.generate *= 2 # Deras generering är nu 2x
  
            elif golden == allUpgrades.fasterEnergy:
              if Values.autoEnergyTimer > 10: # Så att man inte kan få den på 0, skulle sluta fungera annars
                SpriteGoldenPurchase(golden)
                Values.autoEnergyTimer -= 10 # Minska timer för att man ska få energi
                pygame.time.set_timer(autoEnergyEvent, Values.autoEnergyTimer)
                if Values.autoEnergyTimer == 10: # Om det är 10
                  golden.name = 'Maxed!' # Nytt namn
                  golden.cost = 0 # Kostnad
              else: # Samma här
                golden.name = 'Maxed!'
                golden.cost = 0
                pygame.time.set_timer(autoEnergyEvent, Values.autoEnergyTimer)
  
            elif golden == allUpgrades.upgrade50:
              SpriteGoldenPurchase(golden)
              Values.upgradeLessCost *= 2
              for upgrades in upgrades_list:
                upgrades.cost /= Values.upgradeLessCost
                upgrades.originalCost /= Values.upgradeLessCost
                if upgrades.cost < 1 or upgrade.originalCost < 1:
                  upgrades.cost = 0.1
                  upgrades.originalCost = 0.1
  
            elif golden == allUpgrades.energy50:
              SpriteGoldenPurchase(golden)
              Values.incomeLessCost *= 2
              for incomes in incomes_list:
                incomes.cost /= Values.incomeLessCost
                incomes.originalCost /= Values.incomeLessCost
                if incomes.cost < 1 or incomes.originalCost < 1:
                  incomes.cost = 0.1
                  incomes.originalCost = 0.1
      

      else: # Om man inte är i affärs menyn        
        if shopButton.rect.collidepoint(pygame.mouse.get_pos()): # Klickar man på affärsmenyn
          Values.Shop = True # Affärsmenyn är san
        
        if allSprites.energy.rect.collidepoint(pygame.mouse.get_pos()): # Om man trycker på energi ikonen 
          Values.energyNum += 1 * allUpgrades.clicker.upgrade * Values.energyX # Man får 1 energi * om man köpt någon uppgradering (1 från början)

        for sprite in incomes_list: # Går igenom incomes_listan
          if sprite.rect.collidepoint(pygame.mouse.get_pos()): # Ifall man klickar på något i listan
            SpritePurchase(sprite) # Köper den spriten i listan

        if allSprites.evolution.rect.collidepoint(pygame.mouse.get_pos()):
          if Values.energyNum >= allSprites.evolution.required: # Har man mer än vad man behöver? (1 miljon)
            Values.goldenEnergy += Values.energyNum/allSprites.evolution.required # Får golden energy baserat på hur mycket energi man har delat på 1 miljon
            allSprites.evolution.required *= 1.5
            Values.energyNum = 0 # Sätter energi till 0
            Values.autoEnergy = 0 # Sätter auto till 0
            Values.EnergyMultiplier = 1
            
            for sprite in incomes_list: # För varje sprite så:
              sprite.amount = 0 # Mängden man har = 0
              sprite.upgrade = 1 # Upgradenringen = 0
              sprite.cost = sprite.originalCost # Kostnaden = orignalet

            for sprite in upgrades_list: # För varje uppgraderings sprite så:
              sprite.cost = sprite.originalCost # Priset tillbaka till orginalet
  
  Values.screen.fill((30, 25, 50)) # Bakgrundsfärg
  if Values.Shop is False: # Om äffarsmenyn inte är sann riar man det som ska visas + uppdaterar dem
    energy_list.draw(Values.screen) 
    incomes_list.draw(Values.screen)
    shopButton_list.draw(Values.screen)
    evolution_list.draw(Values.screen)

    allSprites.evolution.update()

    for sprites in incomes_list:
      sprites.update() # Uppdaterar varje sprite i loopen

    for sprites in upgrades_list: # För varje sprite i uppgradering
      if Values.energyNum >= sprites.cost: # Om man har mer pengar än någon uppgradering
        exclamationMark_list.draw(Values.screen) # Visar ett utropstecken vid shop-menyn så man vet ifall man kan köpa något

    if Values.energyNum == 0 and Help == 0:
      startArrow_list.draw(Values.screen)

      text = Values.GAME_FONT.render('Click Here', True, Values.TEXT_COLOR) # Text som visar hur mycket den kostar
      textRect = text.get_rect(center=(Values.width /2 + 70, Values.height /2 - 7)) # Placering av texten
      Values.screen.blit(text, textRect) # Talar om vad och var denna text ska visas
      
    else:
      if Values.energyNum > 0 and Help == 0:
        Help = 1
    
  else: # Om den är sann ritar man det andra + uppdaterar dem
    upgrades_list.draw(Values.screen)
    backButton_list.draw(Values.screen)
    goldenUpgrades_list.draw(Values.screen)

    for spriteUpgrades in upgrades_list:
      spriteUpgrades.update() # Uppdaterar varje sprite i loopen

    for spriteGolden in goldenUpgrades_list:
      spriteGolden.update()
  
  allSprites.Energy.show() # Visar alltid energi antal men den har sin egna if Shop i sig själv
  
  pygame.display.flip() # Kan säga att detta uppdaterar skärmen och utan detta skulle inget visas

pygame.quit() # Slut :)