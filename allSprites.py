import pygame
import pygame.freetype
import Values
import makeNumber
# Imporeterar allt nödvändigt
pygame.init()



def showUpdate(sprite, imgName, imgNameDark): # Funktion hur en sprite ska visas + agera när muspekaren nuddar en
  if Values.energyNum >= sprite.cost: # Ifall man har mer/lika mycket energi än kostnaden
    sprite.image = pygame.image.load(imgName).convert() # Laddar in namnet
    sprite.image = pygame.transform.scale(sprite.image,(55,55)) # Skalar om den
    sprite.image.convert_alpha() # Bättre bild? Inte helt 100
  
  else: # Om man inte har tillräckligt
    sprite.image = pygame.image.load(imgNameDark).convert() # Mörkare bilden istället
    sprite.image = pygame.transform.scale(sprite.image,(55,55))
    sprite.image.convert_alpha()
    
  if sprite.rect.collidepoint(pygame.mouse.get_pos()): # Om den nuddar muspekaren
    text = Values.GAME_FONT.render('This costs: ' + makeNumber.numerize(sprite.cost), True, Values.TEXT_COLOR) # Text som visar hur mycket den kostar
    textRect = text.get_rect(center=(Values.width/3 - 11, 50)) # Placering av texten
    Values.screen.blit(text, textRect) # Talar om vad och var denna text ska visas

    belowText = Values.GAME_FONT.render('Generates ' + makeNumber.numerize(sprite.generate * sprite.upgrade * Values.EnergyMultiplier) + '/s', True, Values.TEXT_COLOR) # Samma princip som ovan fast hur mycket per sekund den ger
    belowTextRect = belowText.get_rect(center=(Values.width/3 - 11, 50 + Values.FONT_SIZE))
    Values.screen.blit(belowText, belowTextRect)

    furtherText = Values.GAME_FONT.render('Adds 1 ' + sprite.name, True, Values.TEXT_COLOR)
    furtherTextRect = furtherText.get_rect(center=(Values.width/3 - 11, 50 + Values.FONT_SIZE * 2))
    Values.screen.blit(furtherText, furtherTextRect)



class Energy(pygame.sprite.Sprite):
  def __init__(self):
    pygame.sprite.Sprite.__init__(self)
    self.x = Values.width/3
    self.y = Values.height/2
    self.image = pygame.image.load('imagez/energy.png').convert()
    self.image = pygame.transform.scale(self.image, (70,70))
    self.rect = self.image.get_rect()
    self.rect.x = self.x - 45
    self.rect.y = self.y - 45

  def show(): # Samma princip som funktionen fast texten är inte på samma plats eftersom det är energi antal som ska vara på ett visst ställe + "Energy per second"
    if Values.Shop is False: # Ingen affärsmeny
      showEnergy = Values.GAME_FONT.render(makeNumber.numerize(round(Values.energyNum, 1)) + ' Energy', True, Values.ENERGY_COLOR)
      showEnergyRect = showEnergy.get_rect(center=(Values.width/3 - 11, Values.height - 330 - Values.FONT_SIZE - 5))
      Values.screen.blit(showEnergy, showEnergyRect) # Hur mycket energi man har visas

      showGolden = Values.GAME_FONT.render(makeNumber.numerize(Values.goldenEnergy) + ' Golden Energy', True, Values.GOLDEN_COLOR)
      showGoldenRect = showGolden.get_rect(center=(Values.width/3 - 11, Values.height - 330))
      Values.screen.blit(showGolden, showGoldenRect) # Hur mycket golden energy man har visas

      perSecond = Values.GAME_FONT.render('Energy per second: ' + makeNumber.numerize(Values.autoEnergy, 1), True, (0,0,0), (255,255,255))
      perSecondRect = perSecond.get_rect(center=(Values.width/3 - 11, Values.height - 200))
      Values.screen.blit(perSecond, perSecondRect) # Hur mycket energi per sekund visas

    else: # Det är affärsmeny
      showEnergy = Values.GAME_FONT.render(makeNumber.numerize(round(Values.energyNum, 1)) + ' Energy', True, Values.ENERGY_COLOR)
      showEnergyRect = showEnergy.get_rect(center=(Values.width/2 - 11, 25))
      Values.screen.blit(showEnergy, showEnergyRect)

      showGolden = Values.GAME_FONT.render(makeNumber.numerize(Values.goldenEnergy) + ' Golden Energy', True, Values.GOLDEN_COLOR)
      showGoldenRect = showGolden.get_rect(center=(Values.width/2 - 11, 50))
      Values.screen.blit(showGolden, showGoldenRect)

      perSecond = Values.GAME_FONT.render('Energy per second: ' + makeNumber.numerize(Values.autoEnergy, 1), True, (0,0,0), (255,255,255))
      perSecondRect = perSecond.get_rect(center=(Values.width/2 - 11, 75))
      Values.screen.blit(perSecond, perSecondRect)

  def auto(): # Varje gång den kallas får man 1/10 av energin man skulle fått
    Values.energyNum += Values.autoEnergy/10



class Windmill(pygame.sprite.Sprite):
  def __init__(self):
    pygame.sprite.Sprite.__init__(self)
    self.image = pygame.image.load('imagez/windmill.png').convert()
    self.image = pygame.transform.scale(self.image,(55,55))
    self.rect = self.image.get_rect() # Egen hitbox
    self.rect.y = 1 # Y positionen
    self.rect.x = Values.width - 55*3 - 3 # X positionen
    self.cost = 15 # Hur mycket den kostar
    self.originalCost = 15 # Den orginella kostnaden
    self.generate = 0.3 # Hur mycket den genererar
    self.amount = 0 # Hur många man har
    self.upgrade = 1 # Hur mycket man uppgraderat den
    self.name = "Windmill" # Namnet

  def update(self):
    showUpdate(windmill, 'imagez/windmill.png', 'imagez/windmillDark.png') # Skickar in arguemnten i updattera funktionen



class electricWindmill(pygame.sprite.Sprite):
  def __init__(self):
    pygame.sprite.Sprite.__init__(self)
    self.image = pygame.image.load('imagez/electricWindmill.png').convert()
    self.image = pygame.transform.scale(self.image,(55,55))
    self.image.convert_alpha()
    self.rect = self.image.get_rect()
    self.rect.y = 1
    self.rect.x = Values.width - 55*2 - 2
    self.cost = 100
    self.originalCost = 100
    self.generate = 2
    self.amount = 0
    self.upgrade = 1
    self.name = "Electric Windmill"

  def update(self):
    showUpdate(electricWindmill, 'imagez/electricWindmill.png', 'imagez/electricWindmillDark.png')



class Solarpanel(pygame.sprite.Sprite):
  def __init__(self):
    pygame.sprite.Sprite.__init__(self)
    self.image = pygame.image.load('imagez/solarpanel.jpg').convert()
    self.image = pygame.transform.scale(self.image,(55,55))
    self.image.convert_alpha()
    self.rect = self.image.get_rect()
    self.rect.y = 1
    self.rect.x = Values.width - 55 - 1
    self.cost = 1000
    self.originalCost = 1000
    self.generate = 8
    self.amount = 0
    self.upgrade = 1
    self.name = "Solarpanel"

  def update(self):
    showUpdate(solarpanel, 'imagez/solarpanel.jpg', 'imagez/solarpanelDark.jpg')



class AdvancedSolar(pygame.sprite.Sprite):
  def __init__(self):
    pygame.sprite.Sprite.__init__(self)
    self.image = pygame.image.load('imagez/AdvancedSolar.jpg').convert()
    self.image = pygame.transform.scale(self.image,(55,55))
    self.image.convert_alpha()
    self.rect = self.image.get_rect()
    self.rect.y = 57
    self.rect.x = Values.width - 55*3 - 3
    self.cost = 10000
    self.originalCost = 10000
    self.generate = 64
    self.amount = 0
    self.upgrade = 1
    self.name = "Advanced Solarpanel"

  def update(self):
    showUpdate(advancedSolar, 'imagez/AdvancedSolar.jpg', 'imagez/AdvancedSolarDark.jpg')



class Windpump(pygame.sprite.Sprite):
  def __init__(self):
    pygame.sprite.Sprite.__init__(self)
    self.image = pygame.image.load('imagez/windpump.png').convert()
    self.image = pygame.transform.scale(self.image,(55,55))
    self.image.convert_alpha()
    self.rect = self.image.get_rect()
    self.rect.y = 57
    self.rect.x = Values.width - 55*2 - 2
    self.cost = 100000
    self.originalCost = 100000
    self.generate = 310
    self.amount = 0
    self.upgrade = 1
    self.name = "Windpump"

  def update(self):
    showUpdate(windpump, 'imagez/windpump.png', 'imagez/windpumpDark.png')



class OilRefinery(pygame.sprite.Sprite):
  def __init__(self):
    pygame.sprite.Sprite.__init__(self)
    self.image = pygame.image.load('imagez/oilRefinery.png').convert()
    self.image = pygame.transform.scale(self.image,(55,55))
    self.image.convert_alpha()
    self.rect = self.image.get_rect()
    self.rect.y = 57
    self.rect.x = Values.width - 55 - 1
    self.cost = 1000000
    self.originalCost = 1000000
    self.generate = 1550
    self.amount = 0
    self.upgrade = 1
    self.name = "Oil Refinery"

  def update(self):
    showUpdate(oilRefinery, 'imagez/oilRefinery.png', 'imagez/oilRefineryDark.png')



class Recycling(pygame.sprite.Sprite):
  def __init__(self):
    pygame.sprite.Sprite.__init__(self)
    self.image = pygame.image.load('imagez/recycling.png').convert()
    self.image = pygame.transform.scale(self.image,(55,55))
    self.image.convert_alpha()
    self.rect = self.image.get_rect()
    self.rect.y = 113
    self.rect.x = Values.width - 55*3 - 3
    self.cost = 10000000
    self.originalCost = 10000000
    self.generate = 8450
    self.amount = 0
    self.upgrade = 1
    self.name = "Recycling"

  def update(self):
    showUpdate(recycling, 'imagez/recycling.png', 'imagez/recyclingDark.png')



class Waterwheel(pygame.sprite.Sprite):
  def __init__(self):
    pygame.sprite.Sprite.__init__(self)
    self.image = pygame.image.load('imagez/waterwheel.png').convert()
    self.image = pygame.transform.scale(self.image,(55,55))
    self.image.convert_alpha()
    self.rect = self.image.get_rect()
    self.rect.y = 113
    self.rect.x = Values.width - 55*2 - 2
    self.cost = 100000000
    self.originalCost = 100000000
    self.generate = 46700
    self.amount = 0
    self.upgrade = 1
    self.name = "Waterwheel"

  def update(self):
    showUpdate(waterwheel, 'imagez/waterwheel.png', 'imagez/waterwheelDark.png')



class Bioplant(pygame.sprite.Sprite):
  def __init__(self):
    pygame.sprite.Sprite.__init__(self)
    self.image = pygame.image.load('imagez/bioplant.png').convert()
    self.image = pygame.transform.scale(self.image,(55,55))
    self.image.convert_alpha()
    self.rect = self.image.get_rect()
    self.rect.y = 113
    self.rect.x = Values.width - 55 - 1
    self.cost = 1000000000
    self.originalCost = 1000000000
    self.generate = 265000
    self.amount = 0
    self.upgrade = 1
    self.name = "Bioplant"

  def update(self):
    showUpdate(bioplant, 'imagez/bioplant.png', 'imagez/bioplantDark.png')



class GasFactory(pygame.sprite.Sprite):
  def __init__(self):
    pygame.sprite.Sprite.__init__(self)
    self.image = pygame.image.load('imagez/gasFactory.png').convert()
    self.image = pygame.transform.scale(self.image,(55,55))
    self.image.convert_alpha()
    self.rect = self.image.get_rect()
    self.rect.y = 169
    self.rect.x = Values.width - 55*3 - 3
    self.cost = 10000000000
    self.originalCost = 10000000000
    self.generate = 1750000
    self.amount = 0
    self.upgrade = 1
    self.name = "Gas Factory"

  def update(self):
    showUpdate(gasFactory, 'imagez/gasFactory.png', 'imagez/gasFactoryDark.png')



class ThermalGen(pygame.sprite.Sprite):
  def __init__(self):
    pygame.sprite.Sprite.__init__(self)
    self.image = pygame.image.load('imagez/thermalGen.png').convert()
    self.image = pygame.transform.scale(self.image,(55,55))
    self.image.convert_alpha()
    self.rect = self.image.get_rect()
    self.rect.y = 169
    self.rect.x = Values.width - 55*2 - 2
    self.cost = 100000000000
    self.originalCost = 100000000000
    self.generate = 10000000
    self.amount = 0
    self.upgrade = 1
    self.name = "Thermal Generator"

  def update(self):
    showUpdate(thermalGen, 'imagez/thermalGen.png', 'imagez/thermalGenDark.png')



class OilRig(pygame.sprite.Sprite):
  def __init__(self):
    pygame.sprite.Sprite.__init__(self)
    self.image = pygame.image.load('imagez/oilRig.png').convert()
    self.image = pygame.transform.scale(self.image,(55,55))
    self.image.convert_alpha()
    self.rect = self.image.get_rect()
    self.rect.y = 169
    self.rect.x = Values.width - 55 - 1
    self.cost = 1000000000000
    self.originalCost = 1000000000000
    self.generate = 70500000
    self.amount = 0
    self.upgrade = 1
    self.name = "Oil Rig"

  def update(self):
    showUpdate(oilRig, 'imagez/oilRig.png', 'imagez/oilRigDark.png')



class CoalFactory(pygame.sprite.Sprite):
  def __init__(self):
    pygame.sprite.Sprite.__init__(self)
    self.image = pygame.image.load('imagez/coalplant.png').convert()
    self.image = pygame.transform.scale(self.image,(55,55))
    self.image.convert_alpha()
    self.rect = self.image.get_rect()
    self.rect.y = 225
    self.rect.x = Values.width - 55*3 - 3
    self.cost = 10000000000000
    self.originalCost = 10000000000000
    self.generate = 510000000
    self.amount = 0
    self.upgrade = 1
    self.name = "Coal Factory"

  def update(self):
    showUpdate(coalFactory, 'imagez/coalplant.png', 'imagez/coalplantDark.png')



class WaterDam(pygame.sprite.Sprite):
  def __init__(self):
    pygame.sprite.Sprite.__init__(self)
    self.image = pygame.image.load('imagez/waterDam.png').convert()
    self.image = pygame.transform.scale(self.image,(55,55))
    self.image.convert_alpha()
    self.rect = self.image.get_rect()
    self.rect.y = 225
    self.rect.x = Values.width - 55*2 - 2
    self.cost = 100000000000000
    self.originalCost = 100000000000000
    self.generate = 3350000000
    self.amount = 0
    self.upgrade = 1
    self.name = "Water Dam"

  def update(self):
    showUpdate(waterDam, 'imagez/waterDam.png', 'imagez/waterDamDark.png')



class Workers(pygame.sprite.Sprite):
  def __init__(self):
    pygame.sprite.Sprite.__init__(self)
    self.image = pygame.image.load('imagez/workers.png').convert()
    self.image = pygame.transform.scale(self.image,(55,55))
    self.image.convert_alpha()
    self.rect = self.image.get_rect()
    self.rect.y = 225
    self.rect.x = Values.width - 55 - 1
    self.cost = 1000000000000000
    self.originalCost = 1000000000000000
    self.generate = 26500000000
    self.amount = 0
    self.upgrade = 1
    self.name = "Worker"

  def update(self):
    showUpdate(workers, 'imagez/workers.png', 'imagez/workersDark.png')



class Powerlines(pygame.sprite.Sprite):
  def __init__(self):
    pygame.sprite.Sprite.__init__(self)
    self.image = pygame.image.load('imagez/powerline.png').convert()
    self.image = pygame.transform.scale(self.image,(55,55))
    self.image.convert_alpha()
    self.rect = self.image.get_rect()
    self.rect.y = 281
    self.rect.x = Values.width - 55*3 - 3
    self.cost = 10000000000000000
    self.originalCost = 10000000000000000
    self.generate = 185000000000
    self.amount = 0
    self.upgrade = 1
    self.name = "Powerline"

  def update(self):
    showUpdate(powerlines, 'imagez/powerline.png', 'imagez/powerlineDark.png')



class Nuclear(pygame.sprite.Sprite):
  def __init__(self):
    pygame.sprite.Sprite.__init__(self)
    self.image = pygame.image.load('imagez/nuclear.png').convert()
    self.image = pygame.transform.scale(self.image,(55,55))
    self.image.convert_alpha()
    self.rect = self.image.get_rect()
    self.rect.y = 281
    self.rect.x = Values.width - 55*2 - 2
    self.cost = 100000000000000000
    self.originalCost = 100000000000000000
    self.generate = 1300000000000
    self.amount = 0
    self.upgrade = 1
    self.name = "Nuclear Powerplant"

  def update(self):
    showUpdate(nuclear, 'imagez/nuclear.png', 'imagez/nuclearDark.png')



class Chemicals(pygame.sprite.Sprite):
  def __init__(self):
    pygame.sprite.Sprite.__init__(self)
    self.image = pygame.image.load('imagez/chemicals.png').convert()
    self.image = pygame.transform.scale(self.image,(55,55))
    self.image.convert_alpha()
    self.rect = self.image.get_rect()
    self.rect.y = 281
    self.rect.x = Values.width - 55 - 1
    self.cost = 1000000000000000000
    self.originalCost = 1000000000000000000
    self.generate = 9250000000000
    self.amount = 0
    self.upgrade = 1
    self.name = "Energy Chemical"

  def update(self):
    showUpdate(chemicals, 'imagez/chemicals.png', 'imagez/chemicalsDark.png')



class Atoms(pygame.sprite.Sprite):
  def __init__(self):
    pygame.sprite.Sprite.__init__(self)
    self.image = pygame.image.load('imagez/AtomSplice.png').convert()
    self.image = pygame.transform.scale(self.image,(55,55))
    self.image.convert_alpha()
    self.rect = self.image.get_rect()
    self.rect.y = 337
    self.rect.x = Values.width - 55*3 - 3
    self.cost = 10000000000000000000
    self.originalCost = 10000000000000000000
    self.generate = 74100000000000
    self.amount = 0
    self.upgrade = 1
    self.name = "Atomsplicing"

  def update(self):
    showUpdate(atoms, 'imagez/AtomSplice.png', 'imagez/AtomSpliceDark.png')



class World(pygame.sprite.Sprite):
  def __init__(self):
    pygame.sprite.Sprite.__init__(self)
    self.image = pygame.image.load('imagez/world.png').convert()
    self.image = pygame.transform.scale(self.image,(55,55))
    self.image.convert_alpha()
    self.rect = self.image.get_rect()
    self.rect.y = 337
    self.rect.x = Values.width - 55*2 - 2
    self.cost = 100000000000000000000
    self.originalCost = 100000000000000000000
    self.generate = 669000000000000
    self.amount = 0
    self.upgrade = 1
    self.name = "World"

  def update(self):
    showUpdate(world, 'imagez/world.png', 'imagez/worldDark.png')



class Sun(pygame.sprite.Sprite):
  def __init__(self):
    pygame.sprite.Sprite.__init__(self)
    self.image = pygame.image.load('imagez/theSun.png').convert()
    self.image = pygame.transform.scale(self.image,(55,55))
    self.image.convert_alpha()
    self.rect = self.image.get_rect()
    self.rect.y = 337
    self.rect.x = Values.width - 55 - 1
    self.cost = 1000000000000000000000
    self.originalCost = 1000000000000000000000
    self.generate = 7250000000000000
    self.amount = 0
    self.upgrade = 1
    self.name = "The Sun"

  def update(self):
    showUpdate(sun, 'imagez/theSun.png', 'imagez/theSunDark.png')



class Evolution(pygame.sprite.Sprite):
  def __init__(self):
    pygame.sprite.Sprite.__init__(self)
    self.image = pygame.image.load('imagez/evolution.png').convert()
    self.image = pygame.transform.scale(self.image,(167,55))
    self.image.convert_alpha()
    self.rect = self.image.get_rect()
    self.rect.y = Values.height - 81
    self.rect.x = Values.width - 55*3-3
    self.required = 7500000

  def update(self):
    if Values.energyNum >= self.required:
      self.image = pygame.image.load('imagez/evolution.png').convert()
      self.image = pygame.transform.scale(self.image,(167,55))
      self.image.convert_alpha()
  
    else: # Om man inte har tillräckligt
      self.image = pygame.image.load('imagez/evolutionDark.png').convert()
      self.image = pygame.transform.scale(self.image,(167,55))
      self.image.convert_alpha()

    if self.rect.collidepoint(pygame.mouse.get_pos()): # Om den nuddar muspekaren
      text = Values.GAME_FONT.render('It costs ' + makeNumber.numerize(self.required) + ' to evolve', True, Values.TEXT_COLOR) # Text som visar hur mycket den kostar
      textRect = text.get_rect(center=(Values.width/3 - 11, 50)) # Placering av texten
      Values.screen.blit(text, textRect) # Talar om vad och var denna text ska visas
      if Values.energyNum >= self.required: # Om man har råd
        belowText = Values.GAME_FONT.render('Grants ' + makeNumber.numerize(Values.energyNum/self.required) + ' golden energy', True, Values.TEXT_COLOR) # Samma princip som ovan fast hur mycket per sekund den ger
        belowTextRect = belowText.get_rect(center=(Values.width/3 - 11, 50 + Values.FONT_SIZE))
        Values.screen.blit(belowText, belowTextRect)
    
        furtherText = Values.GAME_FONT.render('Makes you restart', True, Values.TEXT_COLOR)
        furtherTextRect = furtherText.get_rect(center=(Values.width/3 - 11, 50 + Values.FONT_SIZE * 2))
        Values.screen.blit(furtherText, furtherTextRect)
      else: # Om man inte har råd så visar det att man inte får någon "golden energy" alls
        belowText = Values.GAME_FONT.render('Evolving grants 0 golden energy', True, Values.TEXT_COLOR)
        belowTextRect = belowText.get_rect(center=(Values.width/3 - 11, 50 + Values.FONT_SIZE))
        Values.screen.blit(belowText, belowTextRect)


    
windmill = Windmill()
electricWindmill = electricWindmill()
solarpanel = Solarpanel()
energy = Energy()
advancedSolar = AdvancedSolar()
windpump = Windpump()
oilRefinery = OilRefinery()
recycling = Recycling()
waterwheel = Waterwheel()
bioplant = Bioplant()
gasFactory = GasFactory()
thermalGen = ThermalGen()
oilRig = OilRig()
coalFactory = CoalFactory()
waterDam = WaterDam()
workers = Workers()
powerlines = Powerlines()
nuclear = Nuclear()
chemicals = Chemicals()
atoms = Atoms()
world = World()
sun = Sun()
evolution = Evolution()

spriteList = [windmill,
electricWindmill,solarpanel,advancedSolar,windpump,oilRefinery,recycling,waterwheel,bioplant,gasFactory,thermalGen,oilRig,coalFactory,waterDam,workers,powerlines,nuclear,chemicals,atoms,world,sun,evolution]