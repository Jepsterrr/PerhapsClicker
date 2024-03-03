import pygame
import Values
import makeNumber


def showPurchaseUpdate(sprite, imgName, imgNameDark):
    if Values.energyNum >= sprite.cost:
        sprite.image = pygame.image.load(imgName).convert()
        sprite.image = pygame.transform.scale(sprite.image, (55, 55))
        sprite.image.convert_alpha()
    else:
        sprite.image = pygame.image.load(imgNameDark).convert()
        sprite.image = pygame.transform.scale(sprite.image, (55, 55))
        sprite.image.convert_alpha()

    if sprite.rect.collidepoint(pygame.mouse.get_pos()):
        text = Values.GAME_FONT.render(
            'This costs: ' + makeNumber.numerize(sprite.cost), True,
            Values.TEXT_COLOR)
        textRect = text.get_rect(center=(Values.width / 2 - 11,
                                         50 + Values.FONT_SIZE * 2.75))
        Values.screen.blit(text, textRect)

        belowText = Values.GAME_FONT.render('Adds 2x to ' + sprite.name, True,
                                            Values.TEXT_COLOR)
        belowTextRect = belowText.get_rect(center=(Values.width / 2 - 11, 50 +
                                                   Values.FONT_SIZE * 3.75))
        Values.screen.blit(belowText, belowTextRect)


def showGoldenUpdate(
    sprite, imgName, imgNameDark
):  # Samma princip som den ovan fast detta är de speciella upgraderingarna
    if Values.goldenEnergy >= sprite.cost:  # Ifall man har mer/lika mycket golden energy än kostnaden
        sprite.image = pygame.image.load(
            imgName).convert()  # Laddar in bildnamnet
        sprite.image = pygame.transform.scale(sprite.image,
                                              (55, 55))  # Skalar om den
        sprite.image.convert_alpha()  # Bättre bild? Inte helt 100

    else:  # Om man inte har tillräckligt
        sprite.image = pygame.image.load(
            imgNameDark).convert()  # Mörkare bilden istället
        sprite.image = pygame.transform.scale(sprite.image, (55, 55))
        sprite.image.convert_alpha()

    if sprite.rect.collidepoint(pygame.mouse.get_pos()):
        if sprite.cost != 0:  # Alla kommer vara över detta förutom en när man köpt tillräckligt
            text = Values.GAME_FONT.render(
                'This costs: ' + makeNumber.numerize(sprite.cost) +
                ' Golden Energy', True, Values.TEXT_COLOR)
            textRect = text.get_rect(center=(Values.width / 2 - 11,
                                             50 + Values.FONT_SIZE * 2.75))
            Values.screen.blit(text, textRect)

            belowText = Values.GAME_FONT.render(sprite.name, True,
                                                Values.TEXT_COLOR)
            belowTextRect = belowText.get_rect(
                center=(Values.width / 2 - 11, 50 + Values.FONT_SIZE * 3.75))
            Values.screen.blit(belowText, belowTextRect)

        else:  # Designat för class mainframe då man inte får köpa så att den går under 10
            text = Values.GAME_FONT.render('Can´t purchase any more', True,
                                           Values.TEXT_COLOR)
            textRect = text.get_rect(center=(Values.width / 2 - 11,
                                             50 + Values.FONT_SIZE * 2.75))
            Values.screen.blit(text, textRect)

            belowText = Values.GAME_FONT.render(sprite.name, True,
                                                Values.TEXT_COLOR)
            belowTextRect = belowText.get_rect(
                center=(Values.width / 2 - 11, 50 + Values.FONT_SIZE * 3.75))
            Values.screen.blit(belowText, belowTextRect)


class Clicks(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(
            'upgradeImagez/clickUpgrade.jpg').convert()
        self.image = pygame.transform.scale(self.image, (55, 55))
        self.rect = self.image.get_rect()
        self.rect.y = 150
        self.rect.x = Values.width / 2 - 35
        self.cost = 50
        self.originalCost = 50
        self.upgrade = 1
        self.name = "Clicks"

    def update(self):
        showPurchaseUpdate(clicker, 'upgradeImagez/clickUpgrade.jpg',
                           'upgradeImagez/clickUpgradeDark.jpg')


class ProcentualEnergy(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(
            'upgradeImagez/EnergyMultiplier.jpg').convert()
        self.image = pygame.transform.scale(self.image, (55, 55))
        self.rect = self.image.get_rect()
        self.rect.y = Values.height / 2
        self.rect.x = Values.width / 2 - 35
        self.cost = 250
        self.originalCost = 250
        self.name = "Energy Gain"

    def update(self):
        if Values.energyNum >= self.cost:
            self.image = pygame.image.load(
                'upgradeImagez/EnergyMultiplier.jpg').convert()
            self.image = pygame.transform.scale(self.image, (55, 55))
            self.image.convert_alpha()
        else:
            self.image = pygame.image.load(
                'upgradeImagez/EnergyMultiplierDark.jpg').convert()
            self.image = pygame.transform.scale(self.image, (55, 55))
            self.image.convert_alpha()

        if self.rect.collidepoint(pygame.mouse.get_pos()):
            text = Values.GAME_FONT.render(
                'This costs: ' + makeNumber.numerize(self.cost), True,
                Values.TEXT_COLOR)
            textRect = text.get_rect(center=(Values.width / 2 - 11,
                                             300 + Values.FONT_SIZE * 1.25))
            Values.screen.blit(text, textRect)

            belowText = Values.GAME_FONT.render('5% to ' + self.name, True,
                                                Values.TEXT_COLOR)
            belowTextRect = belowText.get_rect(
                center=(Values.width / 2 - 11, 300 + Values.FONT_SIZE * 2.25))
            Values.screen.blit(belowText, belowTextRect)

            furtherbelowText = Values.GAME_FONT.render(
                'Current gain: ' + str(round(Values.EnergyMultiplier * 100)) +
                '%', True, Values.TEXT_COLOR)
            furtherbelowTextRect = furtherbelowText.get_rect(
                center=(Values.width / 2 - 11, 300 + Values.FONT_SIZE * 3.25))
            Values.screen.blit(furtherbelowText, furtherbelowTextRect)


class WindmillUpgrade(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(
            'upgradeImagez/windmillUpgrade.png').convert()
        self.image = pygame.transform.scale(self.image, (55, 55))
        self.rect = self.image.get_rect()
        self.rect.y = 1
        self.rect.x = Values.width - 55 * 3 - 3
        self.cost = 200
        self.originalCost = 200
        self.name = "Windmills"

    def update(self):
        showPurchaseUpdate(windmillUpgrade,
                           'upgradeImagez/windmillUpgrade.png',
                           'upgradeImagez/windmillUpgradeDark.png')


class ElectricWindmillUpgrade(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(
            'upgradeImagez/electricWindmillUpgrade.png').convert()
        self.image = pygame.transform.scale(self.image, (55, 55))
        self.rect = self.image.get_rect()
        self.rect.y = 1
        self.rect.x = Values.width - 55 * 2 - 2
        self.cost = 1000
        self.originalCost = 1000
        self.name = "Electric Windmills"

    def update(self):
        showPurchaseUpdate(electricWindmillUpgrade,
                           'upgradeImagez/electricWindmillUpgrade.png',
                           'upgradeImagez/electricWindmillUpgradeDark.png')


class SolarpanelUpgrade(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(
            'upgradeImagez/solarpanelUpgrade.jpg').convert()
        self.image = pygame.transform.scale(self.image, (55, 55))
        self.rect = self.image.get_rect()
        self.rect.y = 1
        self.rect.x = Values.width - 55 - 1
        self.cost = 11000
        self.originalCost = 11000
        self.name = "Solarpanels"

    def update(self):
        showPurchaseUpdate(solarpanelUpgrade,
                           'upgradeImagez/solarpanelUpgrade.jpg',
                           'upgradeImagez/solarpanelUpgradeDark.jpg')


class AdvancedSolarUpgrade(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(
            'upgradeImagez/AdvancedSolarUpgrade.jpg').convert()
        self.image = pygame.transform.scale(self.image, (55, 55))
        self.rect = self.image.get_rect()
        self.rect.y = 57
        self.rect.x = Values.width - 55 * 3 - 3
        self.cost = 120000
        self.originalCost = 120000
        self.name = "Solarpanels"

    def update(self):
        showPurchaseUpdate(advancedSolarUpgrade,
                           'upgradeImagez/AdvancedSolarUpgrade.jpg',
                           'upgradeImagez/AdvancedSolarUpgradeDark.jpg')


class WindpumpUpgrade(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(
            'upgradeImagez/windpumpUpgrade.png').convert()
        self.image = pygame.transform.scale(self.image, (55, 55))
        self.rect = self.image.get_rect()
        self.rect.y = 57
        self.rect.x = Values.width - 55 * 2 - 2
        self.cost = 1300000
        self.originalCost = 1300000
        self.name = "Windpumps"

    def update(self):
        showPurchaseUpdate(windpumpUpgrade,
                           'upgradeImagez/windpumpUpgrade.png',
                           'upgradeImagez/windpumpUpgradeDark.png')


class OilRefineryUpgrade(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(
            'upgradeImagez/oilRefineryUpgrade.png').convert()
        self.image = pygame.transform.scale(self.image, (55, 55))
        self.rect = self.image.get_rect()
        self.rect.y = 57
        self.rect.x = Values.width - 55 - 1
        self.cost = 14000000
        self.originalCost = 14000000
        self.name = "Oil Refinerys"

    def update(self):
        showPurchaseUpdate(oilRefineryUpgrade,
                           'upgradeImagez/oilRefineryUpgrade.png',
                           'upgradeImagez/oilRefineryUpgradeDark.png')


class RecyclingUpgrade(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(
            'upgradeImagez/recyclingUpgrade.png').convert()
        self.image = pygame.transform.scale(self.image, (55, 55))
        self.rect = self.image.get_rect()
        self.rect.y = 113
        self.rect.x = Values.width - 55 * 3 - 3
        self.cost = 150000000
        self.originalCost = 150000000
        self.name = "Recyclings"

    def update(self):
        showPurchaseUpdate(recyclingUpgrade,
                           'upgradeImagez/recyclingUpgrade.png',
                           'upgradeImagez/recyclingUpgradeDark.png')


class WaterwheelUpgrade(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(
            'upgradeImagez/waterwheelUpgrade.png').convert()
        self.image = pygame.transform.scale(self.image, (55, 55))
        self.rect = self.image.get_rect()
        self.rect.y = 113
        self.rect.x = Values.width - 55 * 2 - 2
        self.cost = 1600000000
        self.originalCost = 1600000000
        self.name = "Waterwheels"

    def update(self):
        showPurchaseUpdate(waterwheelUpgrade,
                           'upgradeImagez/waterwheelUpgrade.png',
                           'upgradeImagez/waterwheelUpgradeDark.png')


class BioplantUpgrade(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(
            'upgradeImagez/bioplantUpgrade.png').convert()
        self.image = pygame.transform.scale(self.image, (55, 55))
        self.rect = self.image.get_rect()
        self.rect.y = 113
        self.rect.x = Values.width - 55 - 1
        self.cost = 17000000000
        self.originalCost = 17000000000
        self.name = "Bioplants"

    def update(self):
        showPurchaseUpdate(bioplantUpgrade,
                           'upgradeImagez/bioplantUpgrade.png',
                           'upgradeImagez/bioplantUpgradeDark.png')


class GasFactoryUpgrade(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(
            'upgradeImagez/gasFactoryUpgrade.png').convert()
        self.image = pygame.transform.scale(self.image, (55, 55))
        self.rect = self.image.get_rect()
        self.rect.y = 169
        self.rect.x = Values.width - 55 * 3 - 3
        self.cost = 180000000000
        self.originalCost = 180000000000
        self.name = "Gas Factories"

    def update(self):
        showPurchaseUpdate(gasFactoryUpgrade,
                           'upgradeImagez/gasFactoryUpgrade.png',
                           'upgradeImagez/gasFactoryUpgradeDark.png')


class ThermalGenUpgrade(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(
            'upgradeImagez/thermalGenUpgrade.png').convert()
        self.image = pygame.transform.scale(self.image, (55, 55))
        self.rect = self.image.get_rect()
        self.rect.y = 169
        self.rect.x = Values.width - 55 * 2 - 2
        self.cost = 1900000000000
        self.originalCost = 1900000000000
        self.name = "Thermal Generators"

    def update(self):
        showPurchaseUpdate(thermalGenUpgrade,
                           'upgradeImagez/thermalGenUpgrade.png',
                           'upgradeImagez/thermalGenUpgradeDark.png')


class OilRigUpgrade(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(
            'upgradeImagez/oilRigUpgrade.png').convert()
        self.image = pygame.transform.scale(self.image, (55, 55))
        self.rect = self.image.get_rect()
        self.rect.y = 169
        self.rect.x = Values.width - 55 - 1
        self.cost = 20000000000000
        self.originalCost = 20000000000000
        self.name = "Oil Rigs"

    def update(self):
        showPurchaseUpdate(oilRigUpgrade, 'upgradeImagez/oilRigUpgrade.png',
                           'upgradeImagez/oilRigUpgradeDark.png')


class CoalFactoryUpgrade(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(
            'upgradeImagez/coalplantUpgrade.png').convert()
        self.image = pygame.transform.scale(self.image, (55, 55))
        self.rect = self.image.get_rect()
        self.rect.y = 225
        self.rect.x = Values.width - 55 * 3 - 3
        self.cost = 210000000000000
        self.originalCost = 210000000000000
        self.name = "Coal Factories"

    def update(self):
        showPurchaseUpdate(coalFactoryUpgrade,
                           'upgradeImagez/coalplantUpgrade.png',
                           'upgradeImagez/coalplantUpgradeDark.png')


class WaterDamUpgrade(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(
            'upgradeImagez/waterDamUpgrade.png').convert()
        self.image = pygame.transform.scale(self.image, (55, 55))
        self.rect = self.image.get_rect()
        self.rect.y = 225
        self.rect.x = Values.width - 55 * 2 - 2
        self.cost = 2200000000000000
        self.originalCost = 2200000000000000
        self.name = "Water dams"

    def update(self):
        showPurchaseUpdate(waterDamUpgrade,
                           'upgradeImagez/waterDamUpgrade.png',
                           'upgradeImagez/waterDamUpgradeDark.png')


class WorkersUpgrade(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(
            'upgradeImagez/workersUpgrade.png').convert()
        self.image = pygame.transform.scale(self.image, (55, 55))
        self.rect = self.image.get_rect()
        self.rect.y = 225
        self.rect.x = Values.width - 55 - 1
        self.cost = 23000000000000000
        self.originalCost = 23000000000000000
        self.name = "Workers"

    def update(self):
        showPurchaseUpdate(workersUpgrade, 'upgradeImagez/workersUpgrade.png',
                           'upgradeImagez/workersUpgradeDark.png')


class PowerlinesUpgrade(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(
            'upgradeImagez/powerlineUpgrade.png').convert()
        self.image = pygame.transform.scale(self.image, (55, 55))
        self.rect = self.image.get_rect()
        self.rect.y = 281
        self.rect.x = Values.width - 55 * 3 - 3
        self.cost = 240000000000000000
        self.originalCost = 240000000000000000
        self.name = "Powerlines"

    def update(self):
        showPurchaseUpdate(powerlinesUpgrade,
                           'upgradeImagez/powerlineUpgrade.png',
                           'upgradeImagez/powerlineUpgradeDark.png')


class NuclearUpgrade(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(
            'upgradeImagez/nuclearUpgrade.png').convert()
        self.image = pygame.transform.scale(self.image, (55, 55))
        self.rect = self.image.get_rect()
        self.rect.y = 281
        self.rect.x = Values.width - 55 * 2 - 2
        self.cost = 2500000000000000000
        self.originalCost = 2500000000000000000
        self.name = "Nuclear Powerplants"

    def update(self):
        showPurchaseUpdate(nuclearUpgrade, 'upgradeImagez/nuclearUpgrade.png',
                           'upgradeImagez/nuclearUpgradeDark.png')


class ChemicalsUpgrade(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(
            'upgradeImagez/chemicalsUpgrade.png').convert()
        self.image = pygame.transform.scale(self.image, (55, 55))
        self.rect = self.image.get_rect()
        self.rect.y = 281
        self.rect.x = Values.width - 55 - 1
        self.cost = 26000000000000000000
        self.originalCost = 26000000000000000000
        self.name = "Energy Chemicals"

    def update(self):
        showPurchaseUpdate(chemicalsUpgrade,
                           'upgradeImagez/chemicalsUpgrade.png',
                           'upgradeImagez/chemicalsUpgradeDark.png')


class AtomsUpgrade(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(
            'upgradeImagez/AtomSpliceUpgrade.png').convert()
        self.image = pygame.transform.scale(self.image, (55, 55))
        self.rect = self.image.get_rect()
        self.rect.y = 337
        self.rect.x = Values.width - 55 * 3 - 3
        self.cost = 270000000000000000000
        self.originalCost = 270000000000000000000
        self.name = "Atomsplicing"

    def update(self):
        showPurchaseUpdate(atomsUpgrade, 'upgradeImagez/AtomSpliceUpgrade.png',
                           'upgradeImagez/AtomSpliceUpgradeDark.png')


class WorldUpgrade(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(
            'upgradeImagez/worldUpgrade.png').convert()
        self.image = pygame.transform.scale(self.image, (55, 55))
        self.rect = self.image.get_rect()
        self.rect.y = 337
        self.rect.x = Values.width - 55 * 2 - 2
        self.cost = 2800000000000000000000
        self.originalCost = 2800000000000000000000
        self.name = "Worlds"

    def update(self):
        showPurchaseUpdate(worldUpgrade, 'upgradeImagez/worldUpgrade.png',
                           'upgradeImagez/worldUpgradeDark.png')


class SunUpgrade(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(
            'upgradeImagez/theSunUpgrade.png').convert()
        self.image = pygame.transform.scale(self.image, (55, 55))
        self.rect = self.image.get_rect()
        self.rect.y = 337
        self.rect.x = Values.width - 55 - 1
        self.cost = 29000000000000000000000
        self.originalCost = 29000000000000000000000
        self.name = "Suns"

    def update(self):
        showPurchaseUpdate(sunUpgrade, 'upgradeImagez/theSunUpgrade.png',
                           'upgradeImagez/theSunUpgradeDark.png')


class Energy2x(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('upgradeImagez/energy2x.png').convert()
        self.image = pygame.transform.scale(self.image, (55, 55))
        self.rect = self.image.get_rect()
        self.rect.y = 150
        self.rect.x = 1
        self.cost = 1
        self.name = "2x Energy Gain"

    def update(self):
        showGoldenUpdate(energy2x, 'upgradeImagez/energy2x.png',
                         'upgradeImagez/energy2xDark.png')


class FasterEnergy(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('upgradeImagez/mainframe.png').convert()
        self.image = pygame.transform.scale(self.image, (55, 55))
        self.rect = self.image.get_rect()
        self.rect.y = 150
        self.rect.x = 112
        self.cost = 0.5
        self.name = "1s Faster Energy Gain"

    def update(self):
        if self.cost > 0:
            showGoldenUpdate(fasterEnergy, 'upgradeImagez/mainframe.png',
                             'upgradeImagez/mainframeDark.png')
        else:
            showGoldenUpdate(fasterEnergy, 'upgradeImagez/mainframeDark.png',
                             'upgradeImagez/mainframeDark.png')


class Upgrade50(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(
            'upgradeImagez/upgrade50%.png').convert()
        self.image = pygame.transform.scale(self.image, (55, 55))
        self.rect = self.image.get_rect()
        self.rect.y = 258
        self.rect.x = 1
        self.cost = 2
        self.name = "Upgrades cost 50% less"

    def update(self):
        showGoldenUpdate(upgrade50, 'upgradeImagez/upgrade50%.png',
                         'upgradeImagez/upgrade50%Dark.png')


class Energy50(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('upgradeImagez/energy50%.png').convert()
        self.image = pygame.transform.scale(self.image, (55, 55))
        self.rect = self.image.get_rect()
        self.rect.y = 258
        self.rect.x = 112
        self.cost = 3
        self.name = "Energy Incomes cost 50% less"

    def update(self):
        showGoldenUpdate(energy50, 'upgradeImagez/energy50%.png',
                         'upgradeImagez/energy50%Dark.png')


clicker = Clicks()
procentualEnergy = ProcentualEnergy()
windmillUpgrade = WindmillUpgrade()
electricWindmillUpgrade = ElectricWindmillUpgrade()
solarpanelUpgrade = SolarpanelUpgrade()
advancedSolarUpgrade = AdvancedSolarUpgrade()
windpumpUpgrade = WindpumpUpgrade()
oilRefineryUpgrade = OilRefineryUpgrade()
recyclingUpgrade = RecyclingUpgrade()
waterwheelUpgrade = WaterwheelUpgrade()
bioplantUpgrade = BioplantUpgrade()
gasFactoryUpgrade = GasFactoryUpgrade()
thermalGenUpgrade = ThermalGenUpgrade()
oilRigUpgrade = OilRigUpgrade()
coalFactoryUpgrade = CoalFactoryUpgrade()
waterDamUpgrade = WaterDamUpgrade()
workersUpgrade = WorkersUpgrade()
powerlinesUpgrade = PowerlinesUpgrade()
nuclearUpgrade = NuclearUpgrade()
chemicalsUpgrade = ChemicalsUpgrade()
atomsUpgrade = AtomsUpgrade()
worldUpgrade = WorldUpgrade()
sunUpgrade = SunUpgrade()
energy2x = Energy2x()
fasterEnergy = FasterEnergy()
upgrade50 = Upgrade50()
energy50 = Energy50()

upgradeSpriteList = [
    windmillUpgrade, electricWindmillUpgrade, solarpanelUpgrade,
    advancedSolarUpgrade, windpumpUpgrade, oilRefineryUpgrade,
    recyclingUpgrade, waterwheelUpgrade, bioplantUpgrade, gasFactoryUpgrade,
    thermalGenUpgrade, oilRigUpgrade, coalFactoryUpgrade, waterDamUpgrade,
    workersUpgrade, powerlinesUpgrade, nuclearUpgrade, chemicalsUpgrade,
    atomsUpgrade, worldUpgrade, sunUpgrade
]
