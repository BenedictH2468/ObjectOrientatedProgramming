import random

class entity():
    def __init__(self, stats, abilityList):
        self._stats = stats
        self._abilityList = abilityList
    def applyAbility(self, choice):
        if choice == 'IGNITE':
            choice = IGNITE()
            return choice
        if choice == 'GLITCH':
            choice = GLITCH()
            return choice
        if choice == 'HACK':
            choice = HACK()
            return choice
        if choice == 'RESTRUCTURE':
            choice = RESTRUCTURE()
            return choice
        if choice == 'SHIELD':
            choice = SHIELD()
            return choice
        if choice == 'SMOG':
            choice = SMOG()
            return choice
        if choice == 'CRUSH':
            choice = CRUSH()
            return choice
        if choice == 'BULK UP':
            choice = BULKUP()
            return choice
        if choice == 'RESUPPLY':
            choice = RESUPPLY()
            return choice
        if choice == 'FOCUS':
            choice = FOCUS()
            return choice
        if choice == 'SMOKESCREEN':
            choice = SMOKESCREEN()
            return choice
        if choice == 'CRYO SNARE':
            choice = CRYOSNARE()
            return choice
        if choice == 'EVISCERATE':
            choice = EVISCERATE()
            return choice
        if choice == 'SHRAPNEL GRENADE':
            choice = SHRAPNELGRENADE()
            return choice
        if choice == 'FUNGAL BLOOM':
            choice = FUNGALBLOOM()
            return choice
class player(entity):
    def __init__(self, stats, abilityList, classRace, itemList, weaponStats):
        super().__init__(stats, abilityList)
        self._classRace = classRace
        self._itemList = itemList
        self._weaponStats = weaponStats
    def useItem(choice, itemPosition):
        if choice == 'MEDKIT':
            value = 20
            stat = 1
        if choice == 'RECONSTRUCTOR':
            value = 50
            stat = 1
        if choice == 'ENERGY DRINK':
            value = 10
            stat = 3
        if choice == 'GLUCOSE SYRINGE':
            value = 25
            stat = 3
        player._stats[stat] += value
        if player._stats[stat - 1] < player._stats[stat]:
            player._stats[stat] = player._stats[stat - 1]
        if stat == 1:
            print('Player has used', choice, 'and now has', player._stats[stat], 'HP')
        else:
            print('Player has used', choice, 'and now has', player._stats[stat], 'SP')
        itemList[itemPosition + 1] -= 1
        if itemList[itemPosition + 1] == 0:
            del itemList[itemPosition]
            del itemList[itemPosition]
        return itemList, userStats
    def chooseRace(self):
        while True:
            choice = input('Select Race: 1) Human, 2) Robot, 3) Lizardman')
            if choice == '1':
                self._classRace[1] = 'HUMAN'
                self._stats[7] +=2
                self._stats[5] +=1
                self._stats[11] -= 0.1
                break
            if choice == '2':
                self._classRace[1] = 'ROBOT'
                self._stats[6] +=2
                self._stats[5] +=1
                self._stats[8] -= 0.1
                self._stats[12] += 0.2
                break
            if choice == '3':
                self._classRace[1] = 'LIZARDMAN'
                self._stats[4] += 2
                self._stats[5] += 1
                self._stats[9] -= 0.1
                break
        return self._classRace, self._stats
    def chooseAction(self):
        actions = []
        abilityUse = False
        itemUse = False
        while len(actions) < 6:
            actionPossible = False
            while actionPossible == False:
                print("Select action", (len(actions) + 1))
                print('''
Attack
Break
Guard
Ability
Item''')
                if len(actions) > 0:
                    print('Undo')
                choice = input('')
                choice = choice.upper()
                if choice == 'ATTACK' or choice == 'BREAK' or choice == 'GUARD':
                    actionPossible = True
                if choice == 'ABILITY' and abilityUse == False:
                    print('Select ability')
                    for x in range(0,len(self._abilityList)):
                        print(self._abilityList[x])
                    choice = input('')
                    choice = choice.upper()
                    for x in range(0,len(self._abilityList)):
                        if choice == self._abilityList[x]:
                            ability = player.applyAbility(choice)
                            if ability._cost > self._stats[3]:
                                print('Not enough sp')
                            else:
                                abilityUse = True
                                actionPossible = True
                if choice == 'ABILITY' and abilityUse == True:
                    print('You can only use one ability each turn')
                if choice == 'ITEM' and itemUse == False:
                    print("Select item")
                    for x in range(0,(len(self._itemList)-1)):
                        if x % 2 == 0 and self._itemList[x+1] > 0:
                            print(self._itemList[x])
                    choice = input('')
                    choice = choice.upper()
                    for x in range(0,(len(self._itemList))):
                        if self._itemList[x] == choice:
                            actionPossible = True
                            itemUse = True
                if choice == 'ITEM' and itemUse == True:
                    print('You can only use one item each turn')
                if choice == 'UNDO' and len(actions) > 0:
                    isAbility = False
                    if actions[(len(actions)-1)] != 'ATTACK'  and actions[(len(actions)-1)] != 'BREAK' and actions[(len(actions)-1)] != 'GUARD':
                        for x in range(0,(len(self._abilityList))):
                            if self._abilityList[x] == actions[(len(actions)-1)]:
                                isAbility = True
                        if isAbility == True:
                            abilityUse = False
                        else:
                            itemUse = False
                    del actions[(len(actions)-1)]
            print('')
            actions.append(choice)
        return actions
class TECHNOMANCER(player):
    def __init__(self, stats=[75, 75, 50, 50, 7, 8, 14, 8, 1.1, 0.8, 0.8, 0.8, 0.8, 0.8], abilityList=['IGNITE', 'GLITCH', 'HACK', 'RESTRUCTURE', 'SHIELD', 'SMOG'], classRace=['TECHNOMANCER',''], itemList=[], weaponStats=['', 0, 0, 0, 0, 0]):
        super().__init__(stats, abilityList, classRace, itemList, weaponStats)
class ENFORCER(player):
    def __init__(self, stats=[130, 130, 30, 30, 10, 12, 6, 6, 0.9, 1, 1, 1, 1, 1.2], abilityList=['CRUSH', 'BULK UP', 'RESUPPLY'], classRace=['ENFORCER', ''], itemList=[], weaponStats=['', 0, 0, 0, 0, 0,]):
        super().__init__(stats, abilityList, classRace, itemList, weaponStats)
class BOUNTYHUNTER(player):
    def __init__(self, stats=[100, 100, 40, 40, 9, 7, 10, 10, 1.1, 0.5, 0.9, 0.9, 0.7, 0.9], abilityList=['FOCUS', 'SMOKESCREEN', 'CRYO SNARE', 'EVISCERATE'], classRace=['BOUNTY HUNTER', ''], itemList=[], weaponStats=['', 0, 0, 0, 0, 0]):
        super().__init__(stats, abilityList, classRace, itemList, weaponStats)
class enemy(entity):
    def __init__(self, stats, abilityList, pattern, name):
        super().__init__(stats, abilityList)
        self._pattern = pattern
        self._name = name
    def chooseAction(self):
        chosen = False
        while chosen == False:
            spUsage = 0
            actions = self._pattern[random.randint(0,(len(self._pattern) - 1))]
            for x in range(0,6):
                if actions[x] != 'ATTACK' and actions[x] != 'BREAK' and actions[x] != 'GUARD':
                    ability = enemy.applyAbility(self, actions[x])
                    spUsage += ability._cost
            if spUsage <= self._stats[3]:
                chosen = True
        return actions
class SPACEPIRATE(enemy):
    def __init__(self, stats=[70, 70, 30, 30, 11, 11, 6, 6, 1, 1, 1, 1, 1.2, 1], abilityList=['SHRAPNEL GRENADE'], pattern=[['ATTACK', 'BREAK', 'ATTACK', 'SHRAPNEL GRENADE', 'GUARD', 'ATTACK'], ['BREAK', 'ATTACK', 'GUARD', 'GUARD', 'ATTACK', 'BREAK'], ['GUARD', 'BREAK', 'ATTACK', 'GUARD', 'BREAK', 'ATTACK']], name='SPACE PIRATE'):
        super().__init__(stats, abilityList, pattern, name)
class BRAINFUNGUS(enemy):
    def __init__(self, stats=[60, 60, 40, 40, 8, 13, 15, 9, 1, 0.5, 1.3, 1.3, 0.8, 1], abilityList=['FUNGAL BLOOM'], pattern=[['GUARD', 'GUARD', 'FUNGAL BLOOM', 'GUARD', 'BREAK', 'BREAK'], ['GUARD', 'FUNGAL BLOOM', 'BREAK', 'GUARD', 'ATTACK', 'GUARD'], ['GUARD', 'BREAK', 'GUARD', 'GUARD', 'ATTACK', 'GUARD']], name='BRAIN FUNGUS'):
        super().__init__(stats, abilityList, pattern, name)
class VOIDWALKER(enemy):
    def __init__(self, stats=[100, 100, 0, 0, 18, 15, 10, 15, 1, 0.9, 0.9, 0.9, 0.9, 0.9, 1.5], abilityList=[], pattern=[['ATTACK', 'ATTACK', 'BREAK', 'BREAK', 'ATTACK', 'ATTACK'], ['ATTACK', 'GUARD', 'ATTACK', 'ATTACK', 'GUARD', 'ATTACK'], ['GUARD', 'ATTACK', 'ATTACK', 'ATTACK', 'ATTACK', 'GUARD']], name='VOID WALKER'):
        super().__init__(stats, abilityList, pattern, name)
class ASSAULTRON(enemy):
    def __init__(self, stats=[100 ,100, 40, 40, 17, 17, 17, 17, 0.8, 0.8, 0.8, 0.8, 1.2, 1.2], abilityList=['EVISCERATE'], pattern=[['ATTACK', 'GUARD', 'ATTACK', 'BREAK', 'ATTACK', 'EVISCERATE'], ['GUARD', 'ATTACK', 'GUARD', 'BREAK', 'GUARD', 'ATTACK'], ['BREAK', 'ATTACK', 'BREAK', 'GUARD', 'BREAK', 'ATTACK']], name='ASSAULTRON'):
        super().__init__(stats, abilityList, pattern, name)
class weapon():
    def __init__(self, stats, equipable):
        self._stats = stats
        self._equipable = equipable
    def equip(self, classRace):
        classAcceptable = False
        for x in range(0,len(self._equipable)):
            if self._equipable[x] == classRace[0]:
                classAcceptable = True
                return self._stats
        if classAcceptable == False:
            print('Sorry, but your class cannot equip this weapon, please choose another')
            return ['',0,0,0,0,0]
    def unequip(self, weaponStats):
        weaponStats = ['',0,0,0,0,0]
        return weaponStats
class DUALPISTOLS(weapon):
    def __init__(self, stats=['Dual Pistols', 5, 0, 0, 2, 2], equipable=['BOUNTY HUNTER', 'TECHNOMANCER']):
        super().__init__(stats, equipable)
class SHOTGUN(weapon):
    def __init__(self, stats=['Shotgun', 5, 2, 2, 0, 0], equipable=['BOUNTY HUNTER', 'ENFORCER']):
        super().__init__(stats, equipable)
class SNIPERRIFLE(weapon):
    def __init__(self, stats=['Sniper Rifle', 5, 2, 0, 0, 2], equipable=['BOUNTY HUNTER']):
        super().__init__(stats, equipable)
class SMG(weapon):
    def __init__(self, stats=['SMG', 5, 0, 2, 2, 0], equipable=['ENFORCER', 'TECHNOMANCER']):
        super().__init__(stats, equipable)
class ability():
    def __init__(self, cost, target, name):
        self._cost = cost
        self._target = target
        self._name = name

    def consumeSP(self, sp):
        return (sp - self._cost)
class heal(ability):
    def __init__(self, cost, target, name, stat, multiplier, movetype):
        super().__init__(cost, target, name)
        self._stat = stat
        self._multiplier = multiplier
        self._movetype = movetype
    def cast(self, userStats, ModUStats):
        newSP = self.consumeSP(userStats[3])
        userStats[1] += (ModUStats[self._stat] * self._multiplier)
        if userStats[1] > userStats[0]:
            userStats[1] = userStats[0]
        return newSP, userStats[1]
class RESTRUCTURE(heal):
    def __init__(self, cost=10, target=0, name='RESTRUCTURE', stat=2, multiplier=2, movetype='HEAL'):
        super().__init__(cost, target, name, stat, multiplier, movetype)
class RESUPPLY(heal):
    def __init__(self, cost=10, target=0, name='RESUPPLY', stat=2, multiplier=3, movetype='HEAL'):
        super().__init__(cost, target, name, stat, multiplier, movetype)
class status(ability):
    def __init__(self, cost, target, name, statmod, turns, movetype):
        super().__init__(cost, target, name)
        self._statmod = statmod
        self._turns = turns
        self._movetype = movetype
    def cast(self, sp, ustatmods, estatmods):
        newSP = self.consumeSP(sp)
        alreadyActive = False
        if self._target == 1:
            for x in range(0, int(len(estatmods) / 3)):
                if estatmods[x] == self._name:
                    alreadyActive = True
                    estatmods[x+2] = self._turns
            if alreadyActive == False:
                estatmods.append(self._name)
                estatmods.append(self._statmod)
                estatmods.append(self._turns)
        else:
            for x in range(0, int(len(ustatmods) / 3)):
                if ustatmods[x] == self._name:
                    alreadyActive = True
                    ustatmods[x+2] = self._turns
            if alreadyActive == False:
                ustatmods.append(self._name)
                ustatmods.append(self._statmod)
                ustatmods.append(self._turns)
        return newSP, ustatmods, estatmods
class HACK(status):
    def __init__(self, cost=10, target=1, name='HACK', statmod=[-3, -3, 0, 0, 0, -0.1, -0.1, -0.1, -0.1, -0.1], turns=3, movetype='STATUS'):
        super().__init__(cost, target, name, statmod, turns, movetype)
class SHIELD(status):
    def __init__(self, cost=5, target=0, name='SHIELD', statmod=[0, 5, 0, 2, -0.3, -0.1, -0.1, -0.1, -0.1, -0.1], turns=2, movetype='STATUS'):
        super().__init__(cost, target, name, statmod, turns, movetype)
class BULKUP(status):
    def __init__(self, cost=10, target=0, name='BULK UP', statmod=[2, 3, 0, 0, -0.2, -0.2, -0.2, -0.2, -0.2, -0.2], turns=3, movetype='STATUS'):
        super().__init__(cost, target, name, statmod, turns, movetype)
class FOCUS(status):
    def __init__(self, cost=5, target=0, name='FOCUS', statmod=[3, 0, 0, 5, 0, -0.1, -0.1, -0.1, -0.1, -0.1], turns=2, movetype='STATUS'):
        super().__init__(cost, target, name, statmod, turns, movetype)
class SMOKESCREEN(status):
    def __init__(self, cost=10, target=1, name='SMOKESCREEN', statmod=[-3, 0, 0, 0, -0.1, 0, 0, 0, 0, 0], turns=4, movetype='STATUS'):
        super().__init__(cost, target, name, statmod, turns, movetype)
class damage(ability):
    def __init__(self, cost, target, name, dmgtype, dmgstat, defstat, dmgmult, defmult, movetype):
        super().__init__(cost, target, name)
        self._dmgtype = dmgtype
        self._dmgstat = dmgstat
        self._defstat = defstat
        self._dmgmult = dmgmult
        self._defmult = defmult
        self._movetype = movetype
    def cast(self, userStats, enemyStats, sp):
        newSP = self.consumeSP(sp)
        dmg = ((userStats[self._dmgstat] * self._dmgmult) - (enemyStats[self._defstat] * self._defmult))
        dmg = int(dmg * enemyStats[self._dmgtype])
        return newSP, dmg
class IGNITE(damage):
    def __init__(self, cost=5, target=1, name='IGNITE', dmgtype=6, dmgstat=2, defstat=1, dmgmult=2, defmult=1, movetype='DMGATTACK'):
        super().__init__(cost, target, name, dmgtype, dmgstat, defstat, dmgmult, defmult, movetype)
class GLITCH(damage):
    def __init__(self, cost=10, target=1, name='GLITCH', dmgtype=8, dmgstat=2, defstat=2, dmgmult=4, defmult=2, movetype='DMGBREAK'):
        super().__init__(cost, target, name, dmgtype, dmgstat, defstat, dmgmult, defmult, movetype)
class SMOG(damage):
    def __init__(self, cost=15, target=1, name='SMOG', dmgtype=5, dmgstat=2, defstat=1, dmgmult=6, defmult=3, movetype='DMGBREAK'):
        super().__init__(cost, target, name, dmgtype, dmgstat, defstat, dmgmult, defmult, movetype)
class CRUSH(damage):
    def __init__(self, cost=10, target=1, name='CRUSH', dmgtype=4, dmgstat=0, defstat=0, dmgmult=5, defmult=4, movetype='DMGBREAK'):
        super().__init__(cost, target, name, dmgtype, dmgstat, defstat, dmgmult, defmult, movetype)
class CRYOSNARE(damage):
    def __init__(self, cost=10, target=1, name='CRYO SNARE', dmgtype=7, dmgstat=2, defstat=1, dmgmult=4, defmult=2, movetype='DMGGUARD'):
        super().__init__(cost, target, name, dmgtype, dmgstat, defstat, dmgmult, defmult, movetype)
class EVISCERATE(damage):
    def __init__(self, cost=20, target=1, name='EVISCERATE', dmgtype=9, dmgstat=3, defstat=3, dmgmult=8, defmult=5, movetype='DMGBREAK'):
        super().__init__(cost, target, name, dmgtype, dmgstat, defstat, dmgmult, defmult, movetype)
class SHRAPNELGRENADE(damage):
    def __init__(self, cost=10, target=1, name='SHRAPNEL GRENADE', dmgtype=4, dmgstat=0, defstat=1, dmgmult=4, defmult=2, movetype='DMGBREAK'):
        super().__init__(cost, target, name, dmgtype, dmgstat, defstat, dmgmult, defmult, movetype)
class FUNGALBLOOM(damage):
    def __init__(self, cost=10, target=1, name='FUNGAL BLOOM', dmgtype=5, dmgstat=2, defstat=1, dmgmult=4, defmult=2, movetype='DMGGUARD'):
        super().__init__(cost, target, name, dmgtype, dmgstat, defstat, dmgmult, defmult, movetype)

def dmgCalc(atkTotal, defTotal, dmgRes):
    atkTotal *=3
    defTotal *=2
    atkTotal -= defTotal
    dmg = int((atkTotal * dmgRes) / 2)
    if dmg < 1:
        dmg = 1
    return dmg
def playerStatCalc(player, playerstatmods):
    newStats = []
    for x in range(0, 10):
        if x < 4:
            newStats.append(player._stats[x+4] + player._weaponStats[x+1] + playerstatmods[x])
            if newStats[x] < 1:
                newStats[x] = 1
        else:
            newStats.append(player._stats[x+4] + playerstatmods[x])
            if newStats[x] < 0.1:
                newStats[x] = 0.1
    return newStats
def monsterStatCalc(monster, monsterstatmods):
    newStats = []
    for x in range(0, 10):
        if x < 4:
            newStats.append(monster._stats[x+4] + monsterstatmods[x])
            if newStats[x] < 1:
                newStats[x] = 1
        else:
            newStats.append(monster._stats[x+4] + monsterstatmods[x])
            if newStats[x] < 0.1:
                newStats[x] = 0.1
    return newStats

def revealAction(enemyActions, luck):
    number = random.randint(1, 100)
    number+= luck
    if number < 31:
        number = 1
    elif number < 81:
        number = 2
    else:
        number = 3
    revealedRounds = []
    while len(revealedRounds) < number:
        round = random.randint(0,5)
        alreadyRevealed = False
        for y in range(0, len(revealedRounds)):
            if revealedRounds[y] == round:
                alreadyRevealed = True
        if alreadyRevealed == False:
            revealedRounds.append(round)
    revealedActions = []
    for x in range(0,6):
        revealed = False
        for y in range(0, len(revealedRounds)):
            if revealedRounds[y] == x:
                revealed = True
        if revealed == False:
            revealedActions.append('______')
        else:
            revealedActions.append(enemyActions[x])
    return revealedActions
while True:
    choice = input('Select class: 1) BOUNTY HUNTER, 2) ENFORCER, 3) TECHNOMANCER\n')
    if choice == '1':
        player = BOUNTYHUNTER()
        break
    if choice == '2':
        player = ENFORCER()
        break
    if choice == '3':
        player = TECHNOMANCER()
        break
player.chooseRace()
while player._weaponStats[0] == '':
    choice = input('Select weapon: 1) Dual Pistols, 2) Shotgun, 3) Sniper Rifle, 4) SMG\n')
    if choice == '1':
        weapon = DUALPISTOLS()
        player._weaponStats = weapon.equip(player._classRace)
    if choice == '2':
        weapon = SHOTGUN()
        player._weaponStats = weapon.equip(player._classRace)
    if choice == '3':
        weapon = SNIPERRIFLE()
        player._weaponStats = weapon.equip(player._classRace)
    if choice == '4':
        weapon = SMG()
        player._weaponStats = weapon.equip(player._classRace)
while True:
    choice = input('Select enemy: 1) Space Pirate, 2) Brain Fungus, 3) Voidwalker, 4) Assaultron\n')
    if choice == '1':
        monster = SPACEPIRATE()
        break
    if choice == '2':
        monster = BRAINFUNGUS()
        break
    if choice == '3':
        monster = VOIDWALKER()
        break
    if choice == '4':
        monster = ASSAULTRON()
        break
#its combat time JIMBO
playerStatMods = []
monsterStatMods = []
player._itemList = ['MEDKIT', 2, 'RECONSTRUCTOR', 1, 'ENERGY DRINK', 2, 'GLUCOSE SYRINGE', 1]
monsterStatModCalc = [0, 0, 0, 0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
playerStatModCalc = [0, 0, 0, 0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
print('Player     HP', player._stats[1], '/', player._stats[0], '     SP', player._stats[3], '/', player._stats[2])
print(monster._name, '    HP', monster._stats[1], '/', monster._stats[0], '     SP', monster._stats[3], '/', monster._stats[2])
while True:
    if monster._stats[1] < 1 or player._stats[1] < 1:
        break
    for x in range(0, int(len(playerStatMods) / 3)):
        playerStatMods[x+2] -= 1
        if playerStatMods[x+2] < 1:
            del playerStatMods[x]
            del playerStatMods[x]
            del playerStatMods[x]
    for x in range(0, int(len(monsterStatMods) / 3)):
        monsterStatMods[x+2] -= 1
        if monsterStatMods[x+2] < 1:
            del monsterStatMods
            del monsterStatMods
            del monsterStatMods
    monsterAction = monster.chooseAction()
    enemyActions = revealAction(monsterAction, playerStatModCalc[3])
    print('Enemy actions:', enemyActions)
    playerAction = player.chooseAction()
    for x in range(0,6):
        input()
        pAbilityUse = False
        monsterStatModCalc = [0, 0, 0, 0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
        playerStatModCalc = [0, 0, 0, 0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
        mods = int(len(playerStatMods) / 3)
        for z in range(0, mods):
            stat = playerStatMods[(3 * z) - 2]
            for y in range(0, 10):
                playerStatModCalc[y] += stat[y]
        mods = int(len(monsterStatMods) / 3)
        for z in range(0, mods):
            stat = monsterStatMods[(3 * z) - 2]
            for y in range(0, 10):
                monsterStatModCalc[y] += stat[y]
        pstats = playerStatCalc(player, playerStatModCalc)
        mstats = monsterStatCalc(monster, monsterStatModCalc)
        if playerAction[x] != 'ATTACK' and playerAction[x] != 'BREAK' and playerAction[x] != 'GUARD':
            for y in range(0, len(player._abilityList)):
                if player._abilityList[y] == playerAction[x]:
                    pAbilityUse = True
            if pAbilityUse == True:
                playerAbility = player.applyAbility(playerAction[x])
                playerAction[x] = playerAbility._movetype
            else:
                itemUsed = playerAction[x]
                playerAction[x] = ''
        if monsterAction[x] != 'ATTACK' and monsterAction[x] != 'BREAK' and monsterAction[x] != 'GUARD':
            monsterAbility = monster.applyAbility(monsterAction[x])
            monsterAction[x] = monsterAbility._movetype

        if monsterAction[x] == 'ATTACK' and playerAction[x] == 'ATTACK':
            print('Both the player and the', monster._name, 'took the ATTACK action')
            player._stats[1] -= dmgCalc(mstats[0], pstats[1], pstats[4])
            monster._stats[1] -= dmgCalc(pstats[0], mstats[1], mstats[4])
        if monsterAction[x] == 'ATTACK' and playerAction[x] == 'BREAK':
            print('The player took the BREAK action and the', monster._name, 'took the ATTACK action')
            player._stats[1] -= dmgCalc(mstats[0], pstats[1], pstats[4])
        if monsterAction[x] == 'ATTACK' and playerAction[x] == 'GUARD':
            print('The player took the GUARD action and the', monster._name, 'took the ATTACK action')
            player._stats[1] -= int(0.1 * dmgCalc(mstats[0], pstats[1], pstats[4]))
            monster._stats[1] -= dmgCalc(pstats[0], mstats[1], mstats[4])
        if monsterAction[x] == 'ATTACK' and playerAction[x] == 'DMGATTACK':
            print('The player used', playerAbility._name, 'and the', monster._name, 'took the ATTACK action')
            player._stats[3], damage = playerAbility.cast(pstats, mstats, player._stats[3])
            monster._stats[1] -= damage
            player._stats[1] -= dmgCalc(mstats[0], pstats[1], pstats[4])
        if monsterAction[x] == 'ATTACK' and playerAction[x] == 'DMGBREAK':
            print('The player used', playerAbility._name, 'and the', monster._name, 'took the ATTACK action')
            player._stats[1] -= dmgCalc(mstats[0], pstats[1], pstats[4])
            print("The player's ability was interrupted")
        if monsterAction[x] == 'ATTACK' and playerAction[x] == 'DMGGUARD':
            print('The player used', playerAbility._name, 'and the', monster._name, 'took the ATTACK action')
            player._stats[1] -= int(0.1 * dmgCalc(mstats[0], pstats[1], mstats[4]))
            player._stats[3], damage = playerAbility.cast(pstats, mstats, player._stats[3])
            monster._stats[1] -= damage
        if monsterAction[x] == 'ATTACK' and playerAction[x] == 'HEAL':
            print('The player used', playerAbility._name, 'and the', monster._name, 'took the ATTACK action')
            player._stats[3], player._stats[1] = playerAbility.cast(player._stats, pstats)
            player._stats[1] -= dmgCalc(mstats[0], pstats[1], pstats[4])
        if monsterAction[x] == 'ATTACK' and playerAction[x] == 'STATUS':
            print('The player used', playerAbility._name, 'and the', monster._name, 'took the ATTACK action')
            player._stats[1] -= dmgCalc(mstats[0], pstats[1], pstats[4])
            player._stats[3], playerStatMods, monsterStatMods  = playerAbility.cast(player._stats[3], playerStatMods, monsterStatMods)
        if monsterAction[x] == 'ATTACK' and playerAction[x] == '':
            player.useItem
            player._stats[1] -= dmgCalc(mstats[0], pstats[1], pstats[4])
        if monsterAction[x] == 'BREAK' and playerAction[x] == 'ATTACK':
            print('The player took the ATTACK action and the', monster._name, 'took the BREAK action')
            monster._stats[1] -= dmgCalc(pstats[0], mstats[1], mstats[4])
        if monsterAction[x] == 'BREAK' and playerAction[x] == 'BREAK':
            print('Both the player and the', monster._name, 'took the BREAK action')
            player._stats[1] -= dmgCalc(mstats[0], pstats[1], pstats[4])
            monster._stats[1] -= dmgCalc(pstats[0], mstats[1], mstats[4])
        if monsterAction[x] == 'BREAK' and playerAction[x] == 'GUARD':
            print('The player took the GUARD action and the', monster._name, 'took the BREAK action')
            player._stats[1] -= dmgCalc(mstats[0], pstats[1], pstats[4])
        if monsterAction[x] == 'BREAK' and playerAction[x] == 'DMGATTACK':
            print('The player used', playerAbility._name, 'and the', monster._name, 'took the BREAK action')
            player._stats[3], damage = playerAbility.cast(pstats, mstats, player._stats[3])
            monster._stats[1] -= damage
        if monsterAction[x] == 'BREAK' and playerAction[x] == 'DMGBREAK':
            print('The player used', playerAbility._name, 'and the', monster._name, 'took the BREAK action')
            player._stats[3], damage = playerAbility.cast(pstats, mstats, player._stats[3])
            monster._stats[1] -= damage
            player._stats[1] -= dmgCalc(mstats[0], pstats[1], pstats[4])
        if monsterAction[x] == 'BREAK' and playerAction[x] == 'DMGGUARD':
            print('The player used', playerAbility._name, 'and the', monster._name, 'took the BREAK action')
            player._stats[1] -= dmgCalc(mstats[0], pstats[1], pstats[4])
            print("The player's ability was interrupted")
        if monsterAction[x] == 'BREAK' and playerAction[x] == 'HEAL':
            print('The player used', playerAbility._name, 'and the', monster._name, 'took the BREAK action')
            player._stats[3], player._stats[1] = playerAbility.cast(player._stats, pstats)
            player._stats[1] -= dmgCalc(mstats[0], pstats[1], pstats[4])
        if monsterAction[x] == 'BREAK' and playerAction[x] == 'STATUS':
            print('The player used', playerAbility._name, 'and the', monster._name, 'took the BREAK action')
            player._stats[1] -= dmgCalc(mstats[0], pstats[1], pstats[4])
            player._stats[3], playerStatMods, monsterStatMods  = playerAbility.cast(player._stats[3], playerStatMods, monsterStatMods)
        if monsterAction[x] == 'BREAK' and playerAction[x] == '':
            player.useItem
            player._stats[1] -= dmgCalc(mstats[0], pstats[1], pstats[4])
        if monsterAction[x] == 'GUARD' and playerAction[x] == 'ATTACK':
            print('The player took the ATTACK action and the', monster._name, 'took the GUARD action')
            monster._stats[1] -= int(0.1 * dmgCalc(pstats[0], mstats[1], mstats[4]))
            player._stats[1] -= dmgCalc(mstats[0], pstats[1], pstats[4])
        if monsterAction[x] == 'GUARD' and playerAction[x] == 'BREAK':
            print('The player took the BREAK action and the', monster._name, 'took the GUARD action')
            monster._stats[1] -= dmgCalc(pstats[0], mstats[1], mstats[4])
        if monsterAction[x] == 'GUARD' and playerAction[x] == 'GUARD':
            print('Both the player and the', monster._name, 'took the GUARD action')
        if monsterAction[x] == 'GUARD' and playerAction[x] == 'DMGATTACK':
            print('The player used', playerAbility._name, 'and the', monster._name, 'took the GUARD action')
            player._stats[3], damage = playerAbility.cast(pstats, mstats, player._stats[3])
            monster._stats[1] -= int(0.1 * damage)
            player._stats[1] -= dmgCalc(mstats[0], pstats[1], pstats[4])
        if monsterAction[x] == 'GUARD' and playerAction[x] == 'DMGBREAK':
            print('The player used', playerAbility._name, 'and the', monster._name, 'took the GUARD action')
            player._stats[3], damage = playerAbility.cast(pstats, mstats, player._stats[3])
            monster._stats[1] -= damage
        if monsterAction[x] == 'GUARD' and playerAction[x] == 'DMGGUARD':
            print('The player used', playerAbility._name, 'and the', monster._name, 'took the GUARD action')
            player._stats[3], damage = playerAbility.cast(pstats, mstats, player._stats[3])
        if monsterAction[x] == 'GUARD' and playerAction[x] == 'HEAL':
            print('The player used', playerAbility._name, 'and the', monster._name, 'took the GUARD action')
            player._stats[3], player._stats[1] = playerAbility.cast(player._stats, pstats)
        if monsterAction[x] == 'GUARD' and playerAction[x] == 'STATUS':
            print('The player used', playerAbility._name, 'and the', monster._name, 'took the GUARD action')
            player._stats[3], playerStatMods, monsterStatMods  = playerAbility.cast(player._stats[3], playerStatMods, monsterStatMods)
        if monsterAction[x] == 'GUARD' and playerAction[x] == '':
            player.useItem
        if monsterAction[x] == 'DMGATTACK' and playerAction[x] == 'ATTACK':
            print('The player took the ATTACK action and the', monster._name, 'used', monsterAbility._name)
            monster._stats[1] -= dmgCalc(pstats[0], mstats[1], mstats[4])
            monster._stats[3], damage = monsterAbility.cast(mstats, pstats, monster._stats[3])
            player._stats[1] -= damage
        if monsterAction[x] == 'DMGATTACK' and playerAction[x] == 'BREAK':
            print('The player took the BREAK action and the', monster._name, 'used', monsterAbility._name)
            monster._stats[3], damage = monsterAbility.cast(mstats, pstats, monster._stats[3])
            player._stats[1] -= damage
        if monsterAction[x] == 'DMGATTACK' and playerAction[x] == 'GUARD':
            print('The player took the GUARD action and the', monster._name, 'used', monsterAbility._name)
            monster._stats[3], damage = monsterAbility.cast(mstats, pstats, monster._stats[3])
            player._stats[1] -= int(0.1 * damage)
            monster._stats[1] -= dmgCalc(pstats[0], mstats[1], mstats[4])
        if monsterAction[x] == 'DMGATTACK' and playerAction[x] == 'DMGATTACK':
            print('The player used', playerAbility._name,' and the', monster._name, 'used', monsterAbility._name)
            player._stats[3], damage = playerAbility.cast(pstats, mstats, player._stats[3])
            monster._stats[1] -= damage
            monster._stats[3], damage = monsterAbility.cast(mstats, pstats, monster._stats[3])
            player._stats[1] -= damage
        if monsterAction[x] == 'DMGATTACK' and playerAction[x] == 'DMGBREAK':
            print('The player used', playerAbility._name,' and the', monster._name, 'used', monsterAbility._name)
            monster._stats[3], damage = monsterAbility.cast(mstats, pstats, monster._stats[3])
            player._stats[1] -= damage
            print("The player's ability was interrupted")
        if monsterAction[x] == 'DMGATTACK' and playerAction[x] == 'DMGGUARD':
            print('The player used', playerAbility._name,' and the', monster._name, 'used', monsterAbility._name)
            monster._stats[3], damage = monsterAbility.cast(mstats, pstats, monster._stats[3])
            player._stats[1] -= int(0.1 * damage)
            player._stats[3], damage = playerAbility.cast(pstats, mstats, player._stats[3])
            monster._stats[1] -= damage
        if monsterAction[x] == 'DMGATTACK' and playerAction[x] == 'HEAL':
            print('The player used', playerAbility._name,' and the', monster._name, 'used', monsterAbility._name)
            player._stats[3], player._stats[1] = playerAbility.cast(player._stats, pstats)
            monster._stats[3], damage = monsterAbility.cast(mstats, pstats, monster._stats[3])
            player._stats[1] -= damage
        if monsterAction[x] == 'DMGATTACK' and playerAction[x] == 'STATUS':
            print('The player used', playerAbility._name,' and the', monster._name, 'used', monsterAbility._name)
            monster._stats[3], damage = monsterAbility.cast(mstats, pstats, monster._stats[3])
            player._stats[1] -= damage
            player._stats[3], playerStatMods, monsterStatMods  = playerAbility.cast(player._stats[3], playerStatMods, monsterStatMods)
        if monsterAction[x] == 'DMGATTACK' and playerAction[x] == '':
            player.useItem
            monster._stats[3], damage = monsterAbility.cast(mstats, pstats, monster._stats[3])
            player._stats[1] -= damage
        if monsterAction[x] == 'DMGBREAK' and playerAction[x] == 'ATTACK':
            print('The player took the ATTACK action and the', monster._name, 'used', monsterAbility._name)
            monster._stats[1] -= dmgCalc(pstats[0], mstats[1], mstats[4])
            print("The", monster._name,"'s ability was interrupted")
        if monsterAction[x] == 'DMGBREAK' and playerAction[x] == 'BREAK':
            print('The player took the BREAK action and the', monster._name, 'used', monsterAbility._name)
            monster._stats[1] -= dmgCalc(pstats[0], mstats[1], mstats[4])
            monster._stats[3], damage = monsterAbility.cast(mstats, pstats, monster._stats[3])
            player._stats[1] -= damage
        if monsterAction[x] == 'DMGBREAK' and playerAction[x] == 'GUARD':
            print('The player took the GUARD action and the', monster._name, 'used', monsterAbility._name)
            monster._stats[3], damage = monsterAbility.cast(mstats, pstats, monster._stats[3])
            player._stats[1] -= damage
        if monsterAction[x] == 'DMGBREAK' and playerAction[x] == 'DMGATTACK':
            print('The player used', playerAbility._name,' and the', monster._name, 'used', monsterAbility._name)
            player._stats[3], damage = playerAbility.cast(pstats, mstats, player._stats[3])
            monster._stats[1] -= damage
            print("The", monster._name,"'s ability was interrupted")
        if monsterAction[x] == 'DMGBREAK' and playerAction[x] == 'DMGBREAK':
            print('The player used', playerAbility._name,' and the', monster._name, 'used', monsterAbility._name)
            player._stats[3], damage = playerAbility.cast(pstats, mstats, player._stats[3])
            monster._stats[1] -= damage
            monster._stats[3], damage = monsterAbility.cast(mstats, pstats, monster._stats[3])
            player._stats[1] -= damage
        if monsterAction[x] == 'DMGBREAK' and playerAction[x] == 'DMGGUARD':
            print('The player used', playerAbility._name,' and the', monster._name, 'used', monsterAbility._name)
            monster._stats[3], damage = monsterAbility.cast(mstats, pstats, monster._stats[3])
            player._stats[1] -= damage
            print("The player's ability was interrupted")
        if monsterAction[x] == 'DMGBREAK' and playerAction[x] == 'HEAL':
            print('The player used', playerAbility._name,' and the', monster._name, 'used', monsterAbility._name)
            player._stats[3], player._stats[1] = playerAbility.cast(player._stats, pstats)
            monster._stats[3], damage = monsterAbility.cast(mstats, pstats, monster._stats[3])
            player._stats[1] -= damage
        if monsterAction[x] == 'DMGBREAK' and playerAction[x] == 'STATUS':
            print('The player used', playerAbility._name,' and the', monster._name, 'used', monsterAbility._name)
            monster._stats[3], damage = monsterAbility.cast(mstats, pstats, monster._stats[3])
            player._stats[1] -= damage
            player._stats[3], playerStatMods, monsterStatMods  = playerAbility.cast(player._stats[3], playerStatMods, monsterStatMods)
        if monsterAction[x] == 'DMGBREAK' and playerAction[x] == '':
            player.useItem
            monster._stats[3], damage = monsterAbility.cast(mstats, pstats, monster._stats[3])
            player._stats[1] -= damage
        if monsterAction[x] == 'DMGGUARD' and playerAction[x] == 'ATTACK':
            print('The player took the ATTACK action and the', monster._name, 'used', monsterAbility._name)
            monster._stats[1] -= int(0.1 * dmgCalc(pstats[0], mstats[1], mstats[4]))
            monster._stats[3], damage = monsterAbility.cast(mstats, pstats, monster._stats[3])
            player._stats[1] -= damage
        if monsterAction[x] == 'DMGGUARD' and playerAction[x] == 'BREAK':
            print('The player took the BREAK action and the', monster._name, 'used', monsterAbility._name)
            monster._stats[1] -= dmgCalc(pstats[0], mstats[1], mstats[4])
            print("The", monster._name, "'s ability was interrupted")
        if monsterAction[x] == 'DMGGUARD' and playerAction[x] == 'GUARD':
            print('The player took the GUARD action and the', monster._name, 'used', monsterAbility._name)
            monster._stats[3], damage = monsterAbility.cast(mstats, pstats, monster._stats[3])
        if monsterAction[x] == 'DMGGUARD' and playerAction[x] == 'DMGATTACK':
            print('The player used', playerAbility._name,' and the', monster._name, 'used', monsterAbility._name)
            player._stats[3], damage = playerAbility.cast(pstats, mstats, player._stats[3])
            monster._stats[1] -= int(0.1 * damage)
            monster._stats[3], damage = monsterAbility.cast(mstats, pstats, monster._stats[3])
            player._stats[1] -= damage
        if monsterAction[x] == 'DMGGUARD' and playerAction[x] == 'DMGBREAK':
            print('The player used', playerAbility._name,' and the', monster._name, 'used', monsterAbility._name)
            player._stats[3], damage = playerAbility.cast(pstats, mstats, player._stats[3])
            monster._stats[1] -= damage
            print("The", monster._name, "'s ability was interrupted")
        if monsterAction[x] == 'DMGGUARD' and playerAction[x] == 'DMGGUARD':
            print('The player used', playerAbility._name,' and the', monster._name, 'used', monsterAbility._name)
            monster._stats[3], damage = monsterAbility.cast(mstats, pstats, monster._stats[3])
            player._stats[3], damage = playerAbility.cast(pstats, mstats, player._stats[3])
        if monsterAction[x] == 'DMGGUARD' and playerAction[x] == 'HEAL':
            print('The player used', playerAbility._name,' and the', monster._name, 'used', monsterAbility._name)
            player._stats[3], player._stats[1] = playerAbility.cast(player._stats, pstats)
            monster._stats[3], damage = monsterAbility.cast(mstats, pstats, monster._stats[3])
        if monsterAction[x] == 'DMGGUARD' and playerAction[x] == 'STATUS':
            print('The player used', playerAbility._name,' and the', monster._name, 'used', monsterAbility._name)
            monster._stats[3], damage = monsterAbility.cast(mstats, pstats, monster._stats[3])
            player._stats[3], playerStatMods, monsterStatMods  = playerAbility.cast(player._stats[3], playerStatMods, monsterStatMods)
        if monsterAction[x] == 'DMGGUARD' and playerAction[x] == '':
            player.useItem
            monster._stats[3], damage = monsterAbility.cast(mstats, pstats, monster._stats[3])
        if monsterAction[x] == 'HEAL' and playerAction[x] == 'ATTACK':
            print('The player took the ATTACK action and the', monster._name, 'used', monsterAbility._name)
            monster._stats[3], monster._stats[1] = monsterAbility.cast(monster._stats, mstats)
            monster._stats[1] -= dmgCalc(pstats[0], mstats[1], mstats[4])
        if monsterAction[x] == 'HEAL' and playerAction[x] == 'BREAK':
            print('The player took the BREAK action and the', monster._name, 'used', monsterAbility._name)
            monster._stats[3], monster._stats[1] = monsterAbility.cast(monster._stats, mstats)
            monster._stats[1] -= dmgCalc(pstats[0], mstats[1], mstats[4])
        if monsterAction[x] == 'HEAL' and playerAction[x] == 'GUARD':
            print('The player took the GUARD action and the', monster._name, 'used', monsterAbility._name)
            monster._stats[3], monster._stats[1] = monsterAbility.cast(monster._stats, mstats)
        if monsterAction[x] == 'HEAL' and playerAction[x] == 'DMGATTACK':
            print('The player used', playerAbility._name,' and the', monster._name, 'used', monsterAbility._name)
            monster._stats[3], monster._stats[1] = monsterAbility.cast(monster._stats, mstats)
            player._stats[3], damage = playerAbility.cast(pstats, mstats, player._stats[3])
            monster._stats[1] -= damage
        if monsterAction[x] == 'HEAL' and playerAction[x] == 'DMGBREAK':
            print('The player used', playerAbility._name,' and the', monster._name, 'used', monsterAbility._name)
            monster._stats[3], monster._stats[1] = monsterAbility.cast(monster._stats, mstats)
            player._stats[3], damage = playerAbility.cast(pstats, mstats, player._stats[3])
            monster._stats[1] -= damage
        if monsterAction[x] == 'HEAL' and playerAction[x] == 'DMGGUARD':
            print('The player used', playerAbility._name,' and the', monster._name, 'used', monsterAbility._name)
            monster._stats[3], monster._stats[1] = monsterAbility.cast(monster._stats, mstats)
            player._stats[3], damage = playerAbility.cast(pstats, mstats, player._stats[3])
        if monsterAction[x] == 'HEAL' and playerAction[x] == 'HEAL':
            print('The player used', playerAbility._name,' and the', monster._name, 'used', monsterAbility._name)
            monster._stats[3], monster._stats[1] = monsterAbility.cast(monster._stats, mstats)
            player._stats[3], player._stats[1] = playerAbility.cast(player._stats, pstats)
        if monsterAction[x] == 'HEAL' and playerAction[x] == 'STATUS':
            print('The player used', playerAbility._name,' and the', monster._name, 'used', monsterAbility._name)
            monster._stats[3], monster._stats[1] = monsterAbility.cast(monster._stats, mstats)
            player._stats[3], playerStatMods, monsterStatMods  = playerAbility.cast(player._stats[3], playerStatMods, monsterStatMods)
        if monsterAction[x] == 'HEAL' and playerAction[x] == '':
            monster._stats[3], monster._stats[1] = monsterAbility.cast(monster._stats, mstats)
            player.useItem
        if monsterAction[x] == 'STATUS' and playerAction[x] == 'ATTACK':
            print('The player took the ATTACK action and the', monster._name, 'used', monsterAbility._name)
            monster._stats[1] -= dmgCalc(pstats[0], mstats[1], mstats[4])
            monster._stats[3], monsterStatMods, playerStatMods  = playerAbility.cast(monster._stats[3], monsterStatMods, playerStatMods)
        if monsterAction[x] == 'STATUS' and playerAction[x] == 'BREAK':
            print('The player took the BREAK action and the', monster._name, 'used', monsterAbility._name)
            monster._stats[1] -= dmgCalc(pstats[0], mstats[1], mstats[4])
            monster._stats[3], monsterStatMods, playerStatMods  = playerAbility.cast(monster._stats[3], monsterStatMods, playerStatMods)
        if monsterAction[x] == 'STATUS' and playerAction[x] == 'GUARD':
            print('The player took the GUARD action and the', monster._name, 'used', monsterAbility._name)
            monster._stats[3], monsterStatMods, playerStatMods  = playerAbility.cast(monster._stats[3], monsterStatMods, playerStatMods)
        if monsterAction[x] == 'STATUS' and playerAction[x] == 'DMGATTACK':
            print('The player used', playerAbility._name,' and the', monster._name, 'used', monsterAbility._name)
            player._stats[3], damage = playerAbility.cast(pstats, mstats, player._stats[3])
            monster._stats[1] -= damage
            monster._stats[3], monsterStatMods, playerStatMods  = playerAbility.cast(monster._stats[3], monsterStatMods, playerStatMods)
        if monsterAction[x] == 'STATUS' and playerAction[x] == 'DMGBREAK':
            print('The player used', playerAbility._name,' and the', monster._name, 'used', monsterAbility._name)
            player._stats[3], damage = playerAbility.cast(pstats, mstats, player._stats[3])
            monster._stats[1] -= damage
            monster._stats[3], monsterStatMods, playerStatMods  = playerAbility.cast(monster._stats[3], monsterStatMods, playerStatMods)
        if monsterAction[x] == 'STATUS' and playerAction[x] == 'DMGGUARD':
            print('The player used', playerAbility._name,' and the', monster._name, 'used', monsterAbility._name)
            player._stats[3], damage = playerAbility.cast(pstats, mstats, player._stats[3])
            monster._stats[3], monsterStatMods, playerStatMods  = playerAbility.cast(monster._stats[3], monsterStatMods, playerStatMods)
        if monsterAction[x] == 'STATUS' and playerAction[x] == 'HEAL':
            print('The player used', playerAbility._name,' and the', monster._name, 'used', monsterAbility._name)
            player._stats[3], player._stats[1] = playerAbility.cast(player._stats, pstats)
            monster._stats[3], monsterStatMods, playerStatMods  = playerAbility.cast(monster._stats[3], monsterStatMods, playerStatMods)
        if monsterAction[x] == 'STATUS' and playerAction[x] == 'STATUS':
            print('The player used', playerAbility._name,' and the', monster._name, 'used', monsterAbility._name)
            player._stats[3], playerStatMods, monsterStatMods  = playerAbility.cast(player._stats[3], playerStatMods, monsterStatMods)
            monster._stats[3], monsterStatMods, playerStatMods  = playerAbility.cast(monster._stats[3], monsterStatMods, playerStatMods)
        if monsterAction[x] == 'STATUS' and playerAction[x] == '':
            player.useItem
            monster._stats[3], monsterStatMods, playerStatMods  = playerAbility.cast(monster._stats[3], monsterStatMods, playerStatMods)
        if monster._stats[1] < 1 or player._stats[1] < 1:
            break
        else:
            print('Player     HP', player._stats[1], '/', player._stats[0], '     SP', player._stats[3], '/', player._stats[2])
            print(monster._name, '    HP', monster._stats[1], '/', monster._stats[0], '     SP', monster._stats[3], '/', monster._stats[2])
if player._stats[1] > 0:
    print('You have killed the', monster._name)
else:
    print('You were killed by the', monster._name)
