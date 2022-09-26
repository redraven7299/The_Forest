import sys
def main():
	#the dictionaries for The_Forest game, player_infomation has objective, age, game_resolution and player_position in it, player_position is the only one that is pre-set due to the game starting in the middle of the playing board. the other dictionary is called enemy, it has the timer for when the enemy get to the Objective and what type the enemy is, when the user chooses what mode they want to play one (18+ or -18).
	player_infomation = {
		"objective": "",
		"age": "",
		"game_resolution": "",
		"player_position": "B2",
	}
	enemy = {
	"timer": "5",
	"enemy_type": "",
	}
	#From line 15 to line 28 is the variables of The_Forest game, there is the age_ovr18 section for when the user chooses 18+ mode and then theres age_undr18 for when the user chooses _18 mode. rge part of each intro/outro are sperated so that the intro/outro can have the objective name that the user chose in it, the winascii and forest2 variables are both ascii art made to make it easiar and cleaner looking (the code to look cleaner) while both message variables are just for the starting homescreen of the game.
	age_ovr18intro = "you are a vampire hunter trying to protect the " 
	age_ovr18introp2 = " from the vampires, get to the " 
	age_ovr18introp3 = " before the vampires do! \n"
	age_ovr18outro = "You have made it back to the "
	age_ovr18outrop2 = " before the vampires could, You were able to set up defences and survived throught the night. You Win!\n"
	age_undr18intro = "You are playing cops & robbers in the forest, If you leave the forest you will be out and lose, Make it to the " 
	age_undr18introp2 = " to win before the cop gets to it first! \n"
	age_undr18outro = "you have made it to the "
	age_undr18outrop2 = " and freed the other robbers, making sure you all help eachother out and bust eachother out of the "
	age_undr18outrop3 = ", winning the game with everyone still in. You Win!"
	winascii = "+-----------------------------------------------------------------------------+ \n|-------------------------------#-----#---------------------------------------| \n|--------------------------------#---#---####--#----#-------------------------| \n|---------------------------------#-#---#----#-#----#-------------------------| \n|----------------------------------#----#----#-#----#-------------------------| \n|----------------------------------#----#----#-#----#-------------------------| \n|----------------------------------#----#----#-#----#-------------------------| \n|----------------------------------#-----####---####--------------------------| \n|-----------------------------------------------------------------------------| \n|-------------------------------#-----#---------------------------------------| \n|-------------------------------#--#--#-#-#----#------------------------------| \n|-------------------------------#--#--#-#-##---#------------------------------| \n|-------------------------------#--#--#-#-#-#--#------------------------------| \n|-------------------------------#--#--#-#-#--#-#------------------------------| \n|-------------------------------#--#--#-#-#---##------------------------------| \n|--------------------------------##-##--#-#----#------------------------------| \n+-----------------------------------------------------------------------------+ \n"
	forest2 = "+--------------------------------------------------------------------------------+ \n|                 . .    ...'..';:;:0WWWMMW0locclcdkxdclx'     lxokcld,,::,..,...| \n|                 ....  ...''..',::c0WWWMMWXxkllkoxOOxclx,     lkodclo,;:;,..'...| \n|                 ....  ...,;'.';lol0WWWMWMNko:cdd0NNXook,     lkll;lo,,cc,......| \n|               ......  .',;l:.,cdxlOWMMWWMNkxlckkKWWWxoO;     ckc:,:l,'cl;......| \n|               ......  .:::xo';oxOdOWWWWMMWkOdo0k0WWWklk:     :k:;',;..;:,......| \n|      .....    ......  .lll0k,;dk0kOWWWWWWWkOol0xOWWWklOc     ,o;,'',..,,..... .| \n| ...  .....    ......  .cll00:,ok0xxXNNXXXXkkdlKOONXNklk:     'c,'..'..,'.......| \n|....  .....    ......  .:lcOO:,lk0xo0K0OOO0dkxcOkxOOKx:o;     .;''.....'.....  .| \n|.... ..'....   ......  .;ccxk:'lxOxlxkkxkxkldo:kxlxdkd;c,     .,''...........   | \n|.''...,;....   ...'..  .;c:dx;.cxkd:oxxddooclo;xdloldo;:,     .,'.......... ..  | \n|.,;'..;c'...   ...'..  .,c:od;.:odl;coollll::c,oo:c:lc','     .'..... ..... .   | \n|.',...';....   ...'..   ,:,:l,.,:lc,:llcccc;;;':c;:::;.''     ....... ..... .   | \n| .... .'....    ..'..   ';,;:'.';c:';c:::::;,,.,;,;;;;...      ....... ....     | \n| .... .'....    .....   .,,,;'..;;;',::::::;,,.';';;;;...      ....... ....     | \n|  ..  ......     ...    .'',,...,;;''::;;;;,',..;';;;;...      ....... ....     | \n| ...........    ..'.    .'.',. .',,..;;;,;;'.'..,',,,,...      ......  ...      | \n|....'',',,'..   .....   ..''....'''..''''','.'..'.,,,,...      ....... ....     | \n|.....................    ..................,,,'',',::;'..      ....... .''. ....| \n|    .........,;:::::,.  .;:::,''''',,'.',,'',,;;;;;;;;'..       .'......','.....| \n|.........,;;::cclccc,   .loll:;:cccc::;;;;:;;;:cc::;:;,,,.      .,,,,'..........| \n|...''',,,;::::;;:c:;... .,:c:;;:cclc::::cc::::cc::::::;,,.      .''''...........| \n|......',,;,,;;;;::c:;,,,',;;:cc:;:clcc:cllcccccc:::::c:;;.      .'',,''''.......| \n|...''''''',,;;::::;:;;;,',,;:c::clcccc::cc:;,:ccccccccc:,.       ..,,''''...... | \n+--------------------------------------------------------------------------------+ \n"
	message = "Welcome to The Forest! \n"
	message = " +-----------------------------------------------------------------------------+ \n |------------------------#######----------------------------------------------| \n |---------------------------#----#----#-######--------------------------------| \n |---------------------------#----#----#-#-------------------------------------| \n |---------------------------#----######-#####---------------------------------| \n |---------------------------#----#----#-#-------------------------------------| \n |---------------------------#----#----#-#-------------------------------------| \n |---------------------------#----#----#-######--------------------------------| \n |-----------------------------------------------------------------------------| \n |---------------#######-#######-######--#######--#####--#######---------------| \n |---------------#-------#-----#-#-----#-#-------#-----#----#------------------| \n |---------------#-------#-----#-#-----#-#-------#----------#------------------| \n |---------------#####---#-----#-######--#####----#####-----#------------------| \n |---------------#-------#-----#-#---#---#-------------#----#------------------| \n |---------------#-------#-----#-#----#--#-------#-----#----#------------------| \n |---------------#-------#######-#-----#-#######--#####-----#------------------| \n +-----------------------------------------------------------------------------+ \n" + message
	# from line 30 to line 70 is the start/intro of The Forest game, from line 30 to line 37 is the start screen. from line 38 to line 49 is what sets the age mode (18+ mode and -18 mode), from line 50 to line 51 sets what the objective building is, from line 52 to from line 69 is what sets the game resolution (it doesnt do anything because of how low the amount of change is.) from line 70 to line 74 is where the intros for each age mode is.
	sys.stdout.write(message)
	sys.stdout.write("are you ready to start to start? \nYes or No? \n")
	start = input()
	if start == "yes":
		sys.stdout.write("Game start! \n")
	elif start == "no":
		sys.stdout.write("ok, bye! \n")
		exit()
	sys.stdout.write("first, are you older than 18? \n")
	age = input()
	if age == "yes":
		player_infomation["age"] = "18+"
		sys.stdout.write("ok, switching to 18+ mode. \n")
		enemy["enemy_type"] = "vampires"
	elif age == "no":
		player_infomation["age"] = "-18"
		sys.stdout.write("ok, switching to -18 mode. \n")
		enemy["enemy_type"] = "cops"
	else:
		exit()
	sys.stdout.write("next, what do you want to call the objective building? \n")
	player_infomation["objective"] = input()
	sys.stdout.write("last part, what do you want to put the game resolution at? \n")
	sys.stdout.write("(between x1 to x1.5) \n")
	game_resolution = input()
	if game_resolution == "x1.5":
		player_infomation["game_resolution"] = "x1.5"
	elif game_resolution == "x1.4":
		player_infomation["game_resolution"] = "x1.4"
	elif game_resolution == "x1.3":
		player_infomation["game_resolution"] = "x1.3"
	elif game_resolution == "x1.2":
		player_infomation["game_resolution"] = "x1.2"
	elif game_resolution == "x1.1":
		player_infomation["game_resolution"] = "x1.1"
	elif game_resolution == "x1":
		player_infomation["game_resolution"] = "x1"
	else:
		sys.stdout.write("not a allowed game resolution!")
		exit()
	sys.stdout.write("alright all done! have fun and don't leave the forest! \n")
	if player_infomation["age"] == "18+":
		sys.stdout.write(age_ovr18intro + player_infomation["objective"] + age_ovr18introp2 + player_infomation["objective"] + age_ovr18introp3)
	elif player_infomation["age"] == "-18":
		sys.stdout.write(age_undr18intro + player_infomation["objective"] + age_undr18introp2 + "\n")
	#between line 76 to line 303 is where the game play is, more specifically from line 76 to line 80 is the start of the game, from line 81 to line 104 is the 2st turn, line 105 to line 170 is the 2nd turn, line 171 to 219 is the 3rd turn, line 220 to line 268 is the 4th turn. line 269 to line 302 is the 5th turn and line 303 to line 304 is a ending, as the enemies have made it to the objective building.
	sys.stdout.write("\n+--------------------------------------------------------------------------------+ \n|.',cxo::;,'',,;ldc;'..''..''';c,';'.;:,......  .''.':;:oo,.....';:;:lc;,;:'..';:| \n|,',cxd::c:,',;:;coc;;'.''''.',;,.''',,.........';cc:;''''...';lc,,::::,'''.....,| \n|c;;coollooc:::c;;cc:lol;,'..;c;;;'.'''.... ....':cldl:,''.',;cc;,,;;'.''''......| \n|loolclodxxl:;:ll::cllx0o;,'.,:;;,..'.......,,...,lxoll:;;,:c:;;;;;::,',,,,...','| \n|odkxccldxdoc:ldkOdc:cool:;'.......''  ..'',:;'.',okl:c,,;;:;;,;;;;,,;;;;,,',cdoc| \n|0OkxdxOkxkOOkxdxxl;,:c;;;,..  ....''..''..,,'',',,;;,;;,,,;:;,;,'...'',,,;;;lolo| \n|KKKkkOO0Okxxxddo;';oOOdlc,.   ....';;c,.'',,''..',,''cc,;cc:::;,;,.....'',,;cc;:| \n|0KWWNKkkkxoldxo,.;oddxkl,.    ....';;;,,;,;:;,''',,,,;:;;::;;:::;''.','.',,;;'',| \n|KXWWNXOdoloolc,';ldlcoo:.   ....;lokd,',;;:c:,'',;,,;::::c::cc:::;,,,,''','''',.| \n|dWWWWNX0doocc;,;::codl;,,.. ....':ldOd,..',;,.,;,,,;::;;;;,;locc;''''''','',,'.'| \n|dWMMMMWNkddc,.';,';oo:'.,....',;:cccloodoooc'.;c;'',;c:,:coooxooo:,'''',;c:,'..;| \n|KWMMMMMNKKk:,;;,,,,'..',. .;,,;:cccclkOkkxo;......,:,';;':c,,''',:::;;;cdc'...,;| \n|ONWMWWMMMNOl::;,::,.......;lccloddodxO00Oko;.......''''..''.....'',;:::cc:'.....| \n|0XNWMWWWWk::c::;;;,'... .'okdoxkOOkO00XNKK0l'''.................'''',;::;,,;,..;| \n|OOOKWNXKOo:llllll;'...  .;odlldxkkkkk0XXXXKd::,';;'...................',..';,.';| \n|kOOKKkxko:clcccc:;'.   ..;clcccodooodOKKXXKx,..',,,........................',,,.| \n|dlokdc:ollkxc,',,,..   ..',,'',;;;;:cdOOkO0k:,'.''''..........  ........''...','| \n|ddlc::colcoc:;'.''.............''',;;cloloddloo;,cc,'.,;'.,,.............,:;'''.| \n|dxdol::::;,,''':l,....''''',,;;::;::ccloodddodddoooo:,;;;,,'.............,:;'','| \n|oddl::;'',;;;;;:c;',:;,,''',,;::;;;;::coodxkkkkkxkOxccl;;lc;'.................',| \n|clc;,,.',;,''cdcdd,.....                  ...',:lxkkxO0dcoooxl,'...............'| \n|lolc;,'';cc;';ocod'...''......       .cdddolodook0KKNWNXXXXNN0kl;:c'........'',:| \n|c:::cc;;:::,'',;::'...;,..,;''... .',;dKNN0kO0kxOXXXNWWWWWWWKOo:;c:......'...'',| \n|:;;,;;;,;,'''.,clc...',,,:dkddlcoooxOxONWWNKXNNNNNNNNWWWWWNXNXOo,:;..'',,..','.'| \n|lc:;;:::::;,;lxkxl....,,,ck00KKO0NXKXXKNWWWNNWMWWWWWWWWWWWNWWNWOoxo':ooOd,','.''| \n|0xllkkkkdc;,;o0K0d,...',;oKXKXWNNNWWWWWWWWWNNNWWWWWWWWWWWWWWWNNX0kddo:xN0xd,...'| \n|0xookkxxd:;;;cxkkx;  .,',d0KKNWWWWWWWWWWWWNNNNWWWWNNWWWWWWWWWWWN0xKXk:cKWXd',:cc| \n+--------------------------------------------------------------------------------+ \n")
	if player_infomation["age"] == "18+":
		sys.stdout.write("you hear the starting bell ringing in the distance, meaning the vampires have started their hunt. you have to make it to the " + player_infomation["objective"] + " quickly or it will fall into the hands of the vampires. \n")
	elif player_infomation["age"] == "-18":
		sys.stdout.write("you hear the starting bell ringing in the distance, meaning the cops have started to move, you have to make it to the " + player_infomation["objective"] + " quickly and free the captured robbers. \n")
	sys.stdout.write("which direction do you want to go?\n" + "(north, east, south, west, do nothing)")
	answer = input("\n-")
	if answer == "north":
		player_infomation["player_position"] = "A2"
		sys.stdout.write("you head north, you are now on A2. north is the edge of the forest, do not cross if you want to win!. \n")
		enemy["timer"] = "4"
	elif answer == "south":
		player_infomation["player_position"] = "C2"
		sys.stdout.write("you head south, you are now on C2. south is the edge of the forest, do not cross if you want to win!. \n")
		enemy["timer"] = "4"
	elif answer == "east":
		player_infomation["player_position"] = "B3"
		sys.stdout.write("you head east, you are now on B3. \n" + "you have found the " + enemy["enemy_type"] + ", you get caught. The End \n")
		sys.stdout.write("+-----------------------------------------------------------------------------+ \n|------------------------#######----------------------------------------------| \n|---------------------------#----#----#-######--------------------------------| \n|---------------------------#----#----#-#-------------------------------------| \n|---------------------------#----######-#####---------------------------------| \n|---------------------------#----#----#-#-------------------------------------| \n|---------------------------#----#----#-#-------------------------------------| \n|---------------------------#----#----#-######--------------------------------| \n|-----------------------------------------------------------------------------| \n|-------------------------#######---------------------------------------------| \n|-------------------------#-------#----#-#####--------------------------------| \n|-------------------------#-------##---#-#----#-------------------------------| \n|-------------------------#####---#-#--#-#----#-------------------------------| \n|-------------------------#-------#--#-#-#----#-------------------------------| \n|-------------------------#-------#---##-#----#-------------------------------| \n|-------------------------#######-#----#-#####--------------------------------| \n+-----------------------------------------------------------------------------+ \n")
		exit()
		enemy["timer"] = "4"
	elif answer == "west":
		player_infomation["player_position"] = "B1"
		sys.stdout.write("you head west, you are now on B1. west is the edge of the forest, do not cross if you want to win!.\n")
		enemy["timer"] = "4"
	elif answer == "do nothing":
		sys.stdout.write("you stand still, trying to hide from everything that moves. \n")
		enemy["timer"] = "4"
	sys.stdout.write("+--------------------------------------------------------------------------------+\n |c;,c:....'';;:l:'',;,;,.',lOWMMWWNKko:,...';:::clxkl;:lcdO0d,;:,;cc;'''';ox:;;..|\n |'.,:;'.....',:dd:;::,;,.':o0WMMMMMNKkl:'''';c::cldoc;:lldxOd;:c,,cc,'''',cl;,;..|\n |..','',....',;oOxoxd:l:',cxKWMMMMMNX0dc,,,,;::cllll:;:::lddl,:c';ol;''',;;''....|\n |....'''....';clOX0Oo:c;';cxXMMMMMMNXOdc,;;;:ccldoll::lc:codd;,:';ol;,,,,,,'..'..|\n |..''.......;clkXKO0d:c,',:dKWMMMMMWX0xl;;:cllllolcc;;lccloxkc;:,,::;,,,,,,'.....|\n |..''..'...'cldOK0OKxco;.,;l0WMMMMWNK0xl:cccloddoc::::lc:lccl::c,';:;;,;;;,,.....|\n |.....''.'',cdkKKOxOdcl;.',:kWMMMMWNKOdlccllcoxxdlcc::c:;ldol;:l;'::,,,;:;:;'....|\n |..,,.''.',;lk0K0xdxc:c,.'',dWMMMMMNKkdc::clodxkxool:;::;cdxd::l;,:c::,',;c:,....|\n |'.,,,;,.',cxOxxkdoo:;c'...'oNMMMMMWXOxc::cldkkxddxdc;;;;:clo::l,';lll:;,,;:,....|\n |,.;c;;,';:dkkkkxddo;;c'....:0WMMMWNX0xl::lookOxoodxoc:;,;clc;;c'.,;cl:;;;:;,....|\n |,.';,,'':cdxooxxddo;:c'....cKMMMMWNXOxl;;looxOOxoodoll:,;::l;';'.';:c;,;:cc,....|\n |,.''';;;loodddkkdoo;::.....lXMMMMMWKkxlcclddxkkOkdlclol:::::;',,.';:l;',;:c;''..|\n |;.'',lccolcodk0Oolo;::.....cKWMMMMWKkdlcldxxxxxxOOdc:clccc::,.,,.,:ll,',,;:;'''.|\n |,.,,;xdod:cxkkOkood::;.....c0NWMMWNKkdc:coxxkkxdkOxl::clooc:'.,,.,cc:,',;;;,.',.|\n |'.;;cOxoo:ckkxOxlox::;.....c0NWMMWNKxo:;;lddxxxddxxdc:;;lddo;',,.;lc:,',,;;,.''.|\n |,.:cokolo:cxxxOxlod::;....'lOXNMMMWKko:,,cdxkkxddddxdo:;clddc,;;',::c:',,;;,.',.|\n |;;oodKdoo;cxxkK0ddd:;,.'..'ck0XWWWWKkd:;:oddxkkxddollxxoolodo:ll,;:;;,,;;::;'',.|\n |;:dodKdoo;ckkkXKxkxc:,''..'cx0XWWWWKkd:;;ldddkkkxxolcdkdddddl:lo:;:::;',;:c:'''.|\n |::dloKdol;lOkkXKxkkc:,.''.'cx0XNWWWXOd:,,lxxdxkkkxdlcoxdxxkxl;coc:c:c;,,,,::;,,.|\n |c:dloKdoo;lOkkNKxkkcc;'...,lxOKXNWNKOdc;;lxxxxxkkkxolododkkko;co:colc:,;,;;,,,;'|\n |::dlo0dol;l0kkNKxOkcc,''.',lxk0XNNNKOdc;:lxxxxxkkkxdodxooxOOd:ld;:oooc;;;;;,'';,|\n |;:dclOool;o0kkNKkOkcc,...',ldx0KXNNKOdc;:lxxxkkkkxxxdxkoodk0xlxx;;codl:::;;;''''|\n |;:xclOool;lOxkNKxkxcc,....,ldx0KXNNKOdc::oxxxkkxxddxdkOoldxOxokO:;clooclc::;'.'.|\n |:;d:cOdoc,lOxxNXxkxc:'....,coxOKXXXKOdc::lxxxxkxddoodkkolooooodxc:cclc:llc:;'.'.|\n |c,o:cxll:'cOdxN0ddo:;'....,lodk0KXXKkoc::ldxxxxxddolodxdooollcodlclcc:;:llc:,''.|\n |c'l;;l;;,':oclxoccc,'.....,lddkO0KX0kl:;;coxkkxxdxxdloxxkdooc:colloolccclooo:,'.|\n |..;,,,.,,,:::clccc:'......,oxxxO0KXKxc;,,:dkOkkxxxddlldxxdolc,;loooollccccclc:;;|\n |',,,,'.,::::::cc::;'......,oxdxO0XWXxc;,;:kX00Okxdoooodddoooc,,:loodolcc:;,,;ccc|\n |,;::c;..::::::::::::......'lxkOXNNXXOc,,,;lxxk00Okdolllloddol::::clooolc:;;;:::;|\n |,,;;;'..,;;::::clodc.......:xO0KK00Odlc:;;:ldxooxOOkkxl;:okxdlllcccloolcc:;;;;;;|\n |'',,'','',,;clc;:ol'.. ....,lddxddoolllllc,,lkOxdooodxxddxxoooollllodxxxdlc:;;;;|\n |....''''',;;::;;::;..     ..,cllcclddddolc;;cd0XXOxl:coddkOkxdlccccldddoddlccc:;|\n |........,;,,,,'''''.       .':lodddxO00xlc::loxOO00Oddollldxkkdc:;;::;;;:::::;::|\n |........'...........        .':cclldk0K00OOo:c:cloxO0Oxdollllcc:,''''',,,,,,,,,,|\n |..'',;,,,..........          ..;:c:cdOKKXK0ocl:;;:;:ccccc::::;;;,......''''..'',|\n |;;;::::;'..........           ..:cclk00kxddoooc'.'..','.'',,,,,,'.....'''.......|\n |',;;;;;'.......'..              .:dkO00kxxdl:dxol:,,.',''...'.',;,'''...........|\n |,,;;,'............               .;okOkkkdlc:oxOx:'............',,''............|\n |.................                ..;ldxxxdoddddxxc........... ..''',,'..........|\n +--------------------------------------------------------------------------------+\n ")
	sys.stdout.write("Turn 2, enemy will get to objective in 4 turns. you are on \n" + player_infomation["player_position"] + ". please choose a direction: north, south, east, west, do nothing")
	answer = input("\n-")
	if answer == "north":
		if player_infomation["player_position"] == "A2":
			sys.stdout.write("you head north, you are now on -A2. you have reached the edge of the forest and found a clearing, stepping into the clearing you hear a loud horn. you left the forest and lost. The End \n")
			sys.stdout.write("+-----------------------------------------------------------------------------+ \n|------------------------#######----------------------------------------------| \n|---------------------------#----#----#-######--------------------------------| \n|---------------------------#----#----#-#-------------------------------------| \n|---------------------------#----######-#####---------------------------------| \n|---------------------------#----#----#-#-------------------------------------| \n|---------------------------#----#----#-#-------------------------------------| \n|---------------------------#----#----#-######--------------------------------| \n|-----------------------------------------------------------------------------| \n|-------------------------#######---------------------------------------------| \n|-------------------------#-------#----#-#####--------------------------------| \n|-------------------------#-------##---#-#----#-------------------------------| \n|-------------------------#####---#-#--#-#----#-------------------------------| \n|-------------------------#-------#--#-#-#----#-------------------------------| \n|-------------------------#-------#---##-#----#-------------------------------| \n|-------------------------#######-#----#-#####--------------------------------| \n+-----------------------------------------------------------------------------+ \n")
			exit()
			enemy["timer"] = "3"
		elif player_infomation["player_position"] == "C2":
			sys.stdout.write("you head north, you are now on B2. \n")
			enemy["timer"] = "3"
		elif player_infomation["player_position"] == "B1":
			sys.stdout.write("you head north, you are now on A3.")
			enemy["timer"] = "3"
	elif answer == "south":
		if player_infomation["player_position"] == "C2":
			sys.stdout.write("you head south, you are now on D2. you have reached the edge of the forest and found a clearing, stepping into the clearing you hear a loud horn. you left the forest and lost. The End \n")
			sys.stdout.write("+-----------------------------------------------------------------------------+ \n|------------------------#######----------------------------------------------| \n|---------------------------#----#----#-######--------------------------------| \n|---------------------------#----#----#-#-------------------------------------| \n|---------------------------#----######-#####---------------------------------| \n|---------------------------#----#----#-#-------------------------------------| \n|---------------------------#----#----#-#-------------------------------------| \n|---------------------------#----#----#-######--------------------------------| \n|-----------------------------------------------------------------------------| \n|-------------------------#######---------------------------------------------| \n|-------------------------#-------#----#-#####--------------------------------| \n|-------------------------#-------##---#-#----#-------------------------------| \n|-------------------------#####---#-#--#-#----#-------------------------------| \n|-------------------------#-------#--#-#-#----#-------------------------------| \n|-------------------------#-------#---##-#----#-------------------------------| \n|-------------------------#######-#----#-#####--------------------------------| \n+-----------------------------------------------------------------------------+ \n")
			exit()
			enemy["timer"] = "3"
		elif player_infomation["player_position"] == "A2":
			sys.stdout.write("you head south, you are now on B2. \n")
			enemy["timer"] = "3"
		elif player_infomation["player_position"] == "B1":
			if player_infomation["age"] == "18+":
				sys.stdout.write("you head south, you are now on C1.\n" + age_ovr18outro + player_infomation["objective"] + age_ovr18outrop2 + "\n" + winascii)
				enemy["timer"] = "3"
				exit()
			elif player_infomation["age"] == "-18":
				sys.stdout.write("you head south, you are now on C1.\n" + age_undr18outro + player_infomation["objective"] + age_undr18outrop2 + age_undr18outrop3 + "\n" + winascii)
				enemy["timer"] = "3"
				exit()
	elif answer == "east":
		if player_infomation["player_position"] == "C2":
			sys.stdout.write("you head east, you are now on C3. \n" + "you have found the " + enemy["enemy_type"] + ", you get caught. The End \n")
			sys.stdout.write("+-----------------------------------------------------------------------------+ \n|------------------------#######----------------------------------------------| \n|---------------------------#----#----#-######--------------------------------| \n|---------------------------#----#----#-#-------------------------------------| \n|---------------------------#----######-#####---------------------------------| \n|---------------------------#----#----#-#-------------------------------------| \n|---------------------------#----#----#-#-------------------------------------| \n|---------------------------#----#----#-######--------------------------------| \n|-----------------------------------------------------------------------------| \n|-------------------------#######---------------------------------------------| \n|-------------------------#-------#----#-#####--------------------------------| \n|-------------------------#-------##---#-#----#-------------------------------| \n|-------------------------#####---#-#--#-#----#-------------------------------| \n|-------------------------#-------#--#-#-#----#-------------------------------| \n|-------------------------#-------#---##-#----#-------------------------------| \n|-------------------------#######-#----#-#####--------------------------------| \n+-----------------------------------------------------------------------------+ \n")
			exit()
			enemy["timer"] = "3"
		elif player_infomation["player_position"] == "A2":
			sys.stdout.write("you head east, you are now on A3. \n")
			enemy["timer"] = "3"
		elif player_infomation["player_position"] == "B1":
			sys.stdout.write("you head east, you are now on B2.")
			enemy["timer"] = "3"
	elif answer == "west":
		if player_infomation["player_position"] == "C2":
			if player_infomation["age"] == "18+":
				sys.stdout.write("you head west, you are now on C1.\n" + age_ovr18outro + player_infomation["objective"] + age_ovr18outrop2 + "\n" + winascii)
				enemy["timer"] = "3"
				exit()
			elif player_infomation["age"] == "-18":
				sys.stdout.write("you head west, you are now on C1.\n" + age_undr18outro + player_infomation["objective"] + age_undr18outrop2 + age_undr18outrop3 + "\n" + winascii)
				enemy["timer"] = "3"
				exit()
		elif player_infomation["player_position"] == "A2":
			sys.stdout.write("you head west, you are now on A1. \n")
			enemy["timer"] = "3"
		elif player_infomation["player_position"] == "B1":
			sys.stdout.write("you head west, you are now on B-0. you have reached the edge of the forest and found a clearing, stepping into the clearing you hear a loud horn. you left the forest and lost. The End \n")
			sys.stdout.write("+-----------------------------------------------------------------------------+ \n|------------------------#######----------------------------------------------| \n|---------------------------#----#----#-######--------------------------------| \n|---------------------------#----#----#-#-------------------------------------| \n|---------------------------#----######-#####---------------------------------| \n|---------------------------#----#----#-#-------------------------------------| \n|---------------------------#----#----#-#-------------------------------------| \n|---------------------------#----#----#-######--------------------------------| \n|-----------------------------------------------------------------------------| \n|-------------------------#######---------------------------------------------| \n|-------------------------#-------#----#-#####--------------------------------| \n|-------------------------#-------##---#-#----#-------------------------------| \n|-------------------------#####---#-#--#-#----#-------------------------------| \n|-------------------------#-------#--#-#-#----#-------------------------------| \n|-------------------------#-------#---##-#----#-------------------------------| \n|-------------------------#######-#----#-#####--------------------------------| \n+-----------------------------------------------------------------------------+ \n")
			exit()
			enemy["timer"] = "3"
	elif answer == "do nothing":
		sys.stdout.write("you stand still, trying to hide from everything that moves. \n")
		enemy["timer"] = "3"
	sys.stdout.write(forest2)
	sys.stdout.write("Turn 3, enemy will get to objective in 2 turns. you are on " + player_infomation["player_position"] + ". please choose a direction: north, south, east, west, do nothing")
	answer = input("\n-")
	if answer == "north":
		if player_infomation["player_position"] == "B2":
			sys.stdout.write("you head north, you are now on A2. \n")
			enemy["timer"] = "2"
		elif player_infomation["player_position"] == "A1":
			sys.stdout.write("you head north, you are now on -A1. you have reached the edge of the forest and found a clearing, stepping into the clearing you hear a loud horn. you left the forest and lost. The End \n")
			sys.stdout.write("+-----------------------------------------------------------------------------+ \n|------------------------#######----------------------------------------------| \n|---------------------------#----#----#-######--------------------------------| \n|---------------------------#----#----#-#-------------------------------------| \n|---------------------------#----######-#####---------------------------------| \n|---------------------------#----#----#-#-------------------------------------| \n|---------------------------#----#----#-#-------------------------------------| \n|---------------------------#----#----#-######--------------------------------| \n|-----------------------------------------------------------------------------| \n|-------------------------#######---------------------------------------------| \n|-------------------------#-------#----#-#####--------------------------------| \n|-------------------------#-------##---#-#----#-------------------------------| \n|-------------------------#####---#-#--#-#----#-------------------------------| \n|-------------------------#-------#--#-#-#----#-------------------------------| \n|-------------------------#-------#---##-#----#-------------------------------| \n|-------------------------#######-#----#-#####--------------------------------| \n+-----------------------------------------------------------------------------+ \n")
			exit()
			enemy["timer"] = "2"
	elif answer == "south":
		if player_infomation["player_position"] == "B2":
			sys.stdout.write("you head south, you are now on C2. \n")
			enemy["timer"] = "2"
	elif answer == "east":
		if player_infomation["player_position"] == "C2":
			sys.stdout.write("you head east, you are now on C3. \n" + "you have found the " + enemy["enemy_type"] + ", you get caught. The End \n")
			sys.stdout.write("+-----------------------------------------------------------------------------+ \n|------------------------#######----------------------------------------------| \n|---------------------------#----#----#-######--------------------------------| \n|---------------------------#----#----#-#-------------------------------------| \n|---------------------------#----######-#####---------------------------------| \n|---------------------------#----#----#-#-------------------------------------| \n|---------------------------#----#----#-#-------------------------------------| \n|---------------------------#----#----#-######--------------------------------| \n|-----------------------------------------------------------------------------| \n|-------------------------#######---------------------------------------------| \n|-------------------------#-------#----#-#####--------------------------------| \n|-------------------------#-------##---#-#----#-------------------------------| \n|-------------------------#####---#-#--#-#----#-------------------------------| \n|-------------------------#-------#--#-#-#----#-------------------------------| \n|-------------------------#-------#---##-#----#-------------------------------| \n|-------------------------#######-#----#-#####--------------------------------| \n+-----------------------------------------------------------------------------+ \n")
			exit()
			enemy["timer"] = "2"
		elif player_infomation["player_position"] == "A2":
			sys.stdout.write("you head east, you are now on A3. \n")
			enemy["timer"] = "2"
		elif player_infomation["player_position"] == "B1":
			sys.stdout.write("you head east, you are now on B2.")
			enemy["timer"] = "2"
	elif answer == "west":
		if player_infomation["player_position"] == "C2":
			if player_infomation["age"] == "18+":
				sys.stdout.write("you head west, you are now on C1.\n" + age_ovr18outro + player_infomation["objective"] + age_ovr18outrop2 + "\n" + winascii)
				enemy["timer"] = "2"
				exit()
			elif player_infomation["age"] == "-18":
				sys.stdout.write("you head west, you are now on C1.\n" + age_undr18outro + player_infomation["objective"] + age_undr18outrop2 + age_undr18outrop3 + "\n" + winascii)
				enemy["timer"] = "2"
				exit()
		elif player_infomation["player_position"] == "A2":
			sys.stdout.write("you head west, you are now on A1. \n")
			enemy["timer"] = "2"
		elif player_infomation["player_position"] == "B1":
			sys.stdout.write("you head west, you are now on B-0. you have reached the edge of the forest and found a clearing, stepping into the clearing you hear a loud horn. you left the forest and lost. The End \n")
			sys.stdout.write("+-----------------------------------------------------------------------------+ \n|------------------------#######----------------------------------------------| \n|---------------------------#----#----#-######--------------------------------| \n|---------------------------#----#----#-#-------------------------------------| \n|---------------------------#----######-#####---------------------------------| \n|---------------------------#----#----#-#-------------------------------------| \n|---------------------------#----#----#-#-------------------------------------| \n|---------------------------#----#----#-######--------------------------------| \n|-----------------------------------------------------------------------------| \n|-------------------------#######---------------------------------------------| \n|-------------------------#-------#----#-#####--------------------------------| \n|-------------------------#-------##---#-#----#-------------------------------| \n|-------------------------#####---#-#--#-#----#-------------------------------| \n|-------------------------#-------#--#-#-#----#-------------------------------| \n|-------------------------#-------#---##-#----#-------------------------------| \n|-------------------------#######-#----#-#####--------------------------------| \n+-----------------------------------------------------------------------------+ \n")
			exit()
			enemy["timer"] = "2"
	elif answer == "do nothing":
		sys.stdout.write("you stand still, trying to hide from everything that moves. \n")
		enemy["timer"] = "2"
	sys.stdout.write("+--------------------------------------------------------------------------------+\n |c;,c:....'';;:l:'',;,;,.',lOWMMWWNKko:,...';:::clxkl;:lcdO0d,;:,;cc;'''';ox:;;..|\n |'.,:;'.....',:dd:;::,;,.':o0WMMMMMNKkl:'''';c::cldoc;:lldxOd;:c,,cc,'''',cl;,;..|\n |..','',....',;oOxoxd:l:',cxKWMMMMMNX0dc,,,,;::cllll:;:::lddl,:c';ol;''',;;''....|\n |....'''....';clOX0Oo:c;';cxXMMMMMMNXOdc,;;;:ccldoll::lc:codd;,:';ol;,,,,,,'..'..|\n |..''.......;clkXKO0d:c,',:dKWMMMMMWX0xl;;:cllllolcc;;lccloxkc;:,,::;,,,,,,'.....|\n |..''..'...'cldOK0OKxco;.,;l0WMMMMWNK0xl:cccloddoc::::lc:lccl::c,';:;;,;;;,,.....|\n |.....''.'',cdkKKOxOdcl;.',:kWMMMMWNKOdlccllcoxxdlcc::c:;ldol;:l;'::,,,;:;:;'....|\n |..,,.''.',;lk0K0xdxc:c,.'',dWMMMMMNKkdc::clodxkxool:;::;cdxd::l;,:c::,',;c:,....|\n |'.,,,;,.',cxOxxkdoo:;c'...'oNMMMMMWXOxc::cldkkxddxdc;;;;:clo::l,';lll:;,,;:,....|\n |,.;c;;,';:dkkkkxddo;;c'....:0WMMMWNX0xl::lookOxoodxoc:;,;clc;;c'.,;cl:;;;:;,....|\n |,.';,,'':cdxooxxddo;:c'....cKMMMMWNXOxl;;looxOOxoodoll:,;::l;';'.';:c;,;:cc,....|\n |,.''';;;loodddkkdoo;::.....lXMMMMMWKkxlcclddxkkOkdlclol:::::;',,.';:l;',;:c;''..|\n |;.'',lccolcodk0Oolo;::.....cKWMMMMWKkdlcldxxxxxxOOdc:clccc::,.,,.,:ll,',,;:;'''.|\n |,.,,;xdod:cxkkOkood::;.....c0NWMMWNKkdc:coxxkkxdkOxl::clooc:'.,,.,cc:,',;;;,.',.|\n |'.;;cOxoo:ckkxOxlox::;.....c0NWMMWNKxo:;;lddxxxddxxdc:;;lddo;',,.;lc:,',,;;,.''.|\n |,.:cokolo:cxxxOxlod::;....'lOXNMMMWKko:,,cdxkkxddddxdo:;clddc,;;',::c:',,;;,.',.|\n |;;oodKdoo;cxxkK0ddd:;,.'..'ck0XWWWWKkd:;:oddxkkxddollxxoolodo:ll,;:;;,,;;::;'',.|\n |;:dodKdoo;ckkkXKxkxc:,''..'cx0XWWWWKkd:;;ldddkkkxxolcdkdddddl:lo:;:::;',;:c:'''.|\n |::dloKdol;lOkkXKxkkc:,.''.'cx0XNWWWXOd:,,lxxdxkkkxdlcoxdxxkxl;coc:c:c;,,,,::;,,.|\n |c:dloKdoo;lOkkNKxkkcc;'...,lxOKXNWNKOdc;;lxxxxxkkkxolododkkko;co:colc:,;,;;,,,;'|\n |::dlo0dol;l0kkNKxOkcc,''.',lxk0XNNNKOdc;:lxxxxxkkkxdodxooxOOd:ld;:oooc;;;;;,'';,|\n |;:dclOool;o0kkNKkOkcc,...',ldx0KXNNKOdc;:lxxxkkkkxxxdxkoodk0xlxx;;codl:::;;;''''|\n |;:xclOool;lOxkNKxkxcc,....,ldx0KXNNKOdc::oxxxkkxxddxdkOoldxOxokO:;clooclc::;'.'.|\n |:;d:cOdoc,lOxxNXxkxc:'....,coxOKXXXKOdc::lxxxxkxddoodkkolooooodxc:cclc:llc:;'.'.|\n |c,o:cxll:'cOdxN0ddo:;'....,lodk0KXXKkoc::ldxxxxxddolodxdooollcodlclcc:;:llc:,''.|\n |c'l;;l;;,':oclxoccc,'.....,lddkO0KX0kl:;;coxkkxxdxxdloxxkdooc:colloolccclooo:,'.|\n |..;,,,.,,,:::clccc:'......,oxxxO0KXKxc;,,:dkOkkxxxddlldxxdolc,;loooollccccclc:;;|\n |',,,,'.,::::::cc::;'......,oxdxO0XWXxc;,;:kX00Okxdoooodddoooc,,:loodolcc:;,,;ccc|\n |,;::c;..::::::::::::......'lxkOXNNXXOc,,,;lxxk00Okdolllloddol::::clooolc:;;;:::;|\n |,,;;;'..,;;::::clodc.......:xO0KK00Odlc:;;:ldxooxOOkkxl;:okxdlllcccloolcc:;;;;;;|\n |'',,'','',,;clc;:ol'.. ....,lddxddoolllllc,,lkOxdooodxxddxxoooollllodxxxdlc:;;;;|\n |....''''',;;::;;::;..     ..,cllcclddddolc;;cd0XXOxl:coddkOkxdlccccldddoddlccc:;|\n |........,;,,,,'''''.       .':lodddxO00xlc::loxOO00Oddollldxkkdc:;;::;;;:::::;::|\n |........'...........        .':cclldk0K00OOo:c:cloxO0Oxdollllcc:,''''',,,,,,,,,,|\n |..'',;,,,..........          ..;:c:cdOKKXK0ocl:;;:;:ccccc::::;;;,......''''..'',|\n |;;;::::;'..........           ..:cclk00kxddoooc'.'..','.'',,,,,,'.....'''.......|\n |',;;;;;'.......'..              .:dkO00kxxdl:dxol:,,.',''...'.',;,'''...........|\n |,,;;,'............               .;okOkkkdlc:oxOx:'............',,''............|\n |.................                ..;ldxxxdoddddxxc........... ..''',,'..........|\n +--------------------------------------------------------------------------------+\n ")
	sys.stdout.write("Turn 4, enemy will get to objective in 2 turns. you are on " + player_infomation["player_position"] + ". please choose a direction: north, south, east, west, do nothing")
	answer = input("\n-")
	if answer == "north":
		if player_infomation["player_position"] == "B2":
			sys.stdout.write("you head north, you are now on A2. \n")
			enemy["timer"] = "2"
		elif player_infomation["player_position"] == "A1":
			sys.stdout.write("you head north, you are now on -A1. you have reached the edge of the forest and found a clearing, stepping into the clearing you hear a loud horn. you left the forest and lost. The End \n")
			sys.stdout.write("+-----------------------------------------------------------------------------+ \n|------------------------#######----------------------------------------------| \n|---------------------------#----#----#-######--------------------------------| \n|---------------------------#----#----#-#-------------------------------------| \n|---------------------------#----######-#####---------------------------------| \n|---------------------------#----#----#-#-------------------------------------| \n|---------------------------#----#----#-#-------------------------------------| \n|---------------------------#----#----#-######--------------------------------| \n|-----------------------------------------------------------------------------| \n|-------------------------#######---------------------------------------------| \n|-------------------------#-------#----#-#####--------------------------------| \n|-------------------------#-------##---#-#----#-------------------------------| \n|-------------------------#####---#-#--#-#----#-------------------------------| \n|-------------------------#-------#--#-#-#----#-------------------------------| \n|-------------------------#-------#---##-#----#-------------------------------| \n|-------------------------#######-#----#-#####--------------------------------| \n+-----------------------------------------------------------------------------+ \n")
			exit()
			enemy["timer"] = "2"
	elif answer == "south":
		if player_infomation["player_position"] == "B2":
			sys.stdout.write("you head south, you are now on C2. \n")
			enemy["timer"] = "2"
	elif answer == "east":
		if player_infomation["player_position"] == "C2":
			sys.stdout.write("you head east, you are now on C3. \n" + "you have found the " + enemy["enemy_type"] + ", you get caught. The End \n")
			sys.stdout.write("+-----------------------------------------------------------------------------+ \n|------------------------#######----------------------------------------------| \n|---------------------------#----#----#-######--------------------------------| \n|---------------------------#----#----#-#-------------------------------------| \n|---------------------------#----######-#####---------------------------------| \n|---------------------------#----#----#-#-------------------------------------| \n|---------------------------#----#----#-#-------------------------------------| \n|---------------------------#----#----#-######--------------------------------| \n|-----------------------------------------------------------------------------| \n|-------------------------#######---------------------------------------------| \n|-------------------------#-------#----#-#####--------------------------------| \n|-------------------------#-------##---#-#----#-------------------------------| \n|-------------------------#####---#-#--#-#----#-------------------------------| \n|-------------------------#-------#--#-#-#----#-------------------------------| \n|-------------------------#-------#---##-#----#-------------------------------| \n|-------------------------#######-#----#-#####--------------------------------| \n+-----------------------------------------------------------------------------+ \n")
			exit()
			enemy["timer"] = "2"
		elif player_infomation["player_position"] == "A2":
			sys.stdout.write("you head east, you are now on A3. \n")
			enemy["timer"] = "2"
		elif player_infomation["player_position"] == "B1":
			sys.stdout.write("you head east, you are now on B2.")
			enemy["timer"] = "2"
	elif answer == "west":
		if player_infomation["player_position"] == "C2":
			if player_infomation["age"] == "18+":
				sys.stdout.write("you head west, you are now on C1.\n" + age_ovr18outro + player_infomation["objective"] + age_ovr18outrop2 + "\n" + winascii)
				enemy["timer"] = "2"
				exit()
			elif player_infomation["age"] == "-18":
				sys.stdout.write("you head west, you are now on C1.\n" + age_undr18outro + player_infomation["objective"] + age_undr18outrop2 + age_undr18outrop3 + "\n" + winascii)
				enemy["timer"] = "2"
				exit()
		elif player_infomation["player_position"] == "A2":
			sys.stdout.write("you head west, you are now on A1. \n")
			enemy["timer"] = "2"
		elif player_infomation["player_position"] == "B1":
			sys.stdout.write("you head west, you are now on B-0. you have reached the edge of the forest and found a clearing, stepping into the clearing you hear a loud horn. you left the forest and lost. The End \n")
			sys.stdout.write("+-----------------------------------------------------------------------------+ \n|------------------------#######----------------------------------------------| \n|---------------------------#----#----#-######--------------------------------| \n|---------------------------#----#----#-#-------------------------------------| \n|---------------------------#----######-#####---------------------------------| \n|---------------------------#----#----#-#-------------------------------------| \n|---------------------------#----#----#-#-------------------------------------| \n|---------------------------#----#----#-######--------------------------------| \n|-----------------------------------------------------------------------------| \n|-------------------------#######---------------------------------------------| \n|-------------------------#-------#----#-#####--------------------------------| \n|-------------------------#-------##---#-#----#-------------------------------| \n|-------------------------#####---#-#--#-#----#-------------------------------| \n|-------------------------#-------#--#-#-#----#-------------------------------| \n|-------------------------#-------#---##-#----#-------------------------------| \n|-------------------------#######-#----#-#####--------------------------------| \n+-----------------------------------------------------------------------------+ \n")
			exit()
			enemy["timer"] = "2"
	elif answer == "do nothing":
		sys.stdout.write("you stand still, trying to hide from everything that moves. \n")
		enemy["timer"] = "2"
	sys.stdout.write("+--------------------------------------------------------------------------------+\n |c;,c:....'';;:l:'',;,;,.',lOWMMWWNKko:,...';:::clxkl;:lcdO0d,;:,;cc;'''';ox:;;..|\n |'.,:;'.....',:dd:;::,;,.':o0WMMMMMNKkl:'''';c::cldoc;:lldxOd;:c,,cc,'''',cl;,;..|\n |..','',....',;oOxoxd:l:',cxKWMMMMMNX0dc,,,,;::cllll:;:::lddl,:c';ol;''',;;''....|\n |....'''....';clOX0Oo:c;';cxXMMMMMMNXOdc,;;;:ccldoll::lc:codd;,:';ol;,,,,,,'..'..|\n |..''.......;clkXKO0d:c,',:dKWMMMMMWX0xl;;:cllllolcc;;lccloxkc;:,,::;,,,,,,'.....|\n |..''..'...'cldOK0OKxco;.,;l0WMMMMWNK0xl:cccloddoc::::lc:lccl::c,';:;;,;;;,,.....|\n |.....''.'',cdkKKOxOdcl;.',:kWMMMMWNKOdlccllcoxxdlcc::c:;ldol;:l;'::,,,;:;:;'....|\n |..,,.''.',;lk0K0xdxc:c,.'',dWMMMMMNKkdc::clodxkxool:;::;cdxd::l;,:c::,',;c:,....|\n |'.,,,;,.',cxOxxkdoo:;c'...'oNMMMMMWXOxc::cldkkxddxdc;;;;:clo::l,';lll:;,,;:,....|\n |,.;c;;,';:dkkkkxddo;;c'....:0WMMMWNX0xl::lookOxoodxoc:;,;clc;;c'.,;cl:;;;:;,....|\n |,.';,,'':cdxooxxddo;:c'....cKMMMMWNXOxl;;looxOOxoodoll:,;::l;';'.';:c;,;:cc,....|\n |,.''';;;loodddkkdoo;::.....lXMMMMMWKkxlcclddxkkOkdlclol:::::;',,.';:l;',;:c;''..|\n |;.'',lccolcodk0Oolo;::.....cKWMMMMWKkdlcldxxxxxxOOdc:clccc::,.,,.,:ll,',,;:;'''.|\n |,.,,;xdod:cxkkOkood::;.....c0NWMMWNKkdc:coxxkkxdkOxl::clooc:'.,,.,cc:,',;;;,.',.|\n |'.;;cOxoo:ckkxOxlox::;.....c0NWMMWNKxo:;;lddxxxddxxdc:;;lddo;',,.;lc:,',,;;,.''.|\n |,.:cokolo:cxxxOxlod::;....'lOXNMMMWKko:,,cdxkkxddddxdo:;clddc,;;',::c:',,;;,.',.|\n |;;oodKdoo;cxxkK0ddd:;,.'..'ck0XWWWWKkd:;:oddxkkxddollxxoolodo:ll,;:;;,,;;::;'',.|\n |;:dodKdoo;ckkkXKxkxc:,''..'cx0XWWWWKkd:;;ldddkkkxxolcdkdddddl:lo:;:::;',;:c:'''.|\n |::dloKdol;lOkkXKxkkc:,.''.'cx0XNWWWXOd:,,lxxdxkkkxdlcoxdxxkxl;coc:c:c;,,,,::;,,.|\n |c:dloKdoo;lOkkNKxkkcc;'...,lxOKXNWNKOdc;;lxxxxxkkkxolododkkko;co:colc:,;,;;,,,;'|\n |::dlo0dol;l0kkNKxOkcc,''.',lxk0XNNNKOdc;:lxxxxxkkkxdodxooxOOd:ld;:oooc;;;;;,'';,|\n |;:dclOool;o0kkNKkOkcc,...',ldx0KXNNKOdc;:lxxxkkkkxxxdxkoodk0xlxx;;codl:::;;;''''|\n |;:xclOool;lOxkNKxkxcc,....,ldx0KXNNKOdc::oxxxkkxxddxdkOoldxOxokO:;clooclc::;'.'.|\n |:;d:cOdoc,lOxxNXxkxc:'....,coxOKXXXKOdc::lxxxxkxddoodkkolooooodxc:cclc:llc:;'.'.|\n |c,o:cxll:'cOdxN0ddo:;'....,lodk0KXXKkoc::ldxxxxxddolodxdooollcodlclcc:;:llc:,''.|\n |c'l;;l;;,':oclxoccc,'.....,lddkO0KX0kl:;;coxkkxxdxxdloxxkdooc:colloolccclooo:,'.|\n |..;,,,.,,,:::clccc:'......,oxxxO0KXKxc;,,:dkOkkxxxddlldxxdolc,;loooollccccclc:;;|\n |',,,,'.,::::::cc::;'......,oxdxO0XWXxc;,;:kX00Okxdoooodddoooc,,:loodolcc:;,,;ccc|\n |,;::c;..::::::::::::......'lxkOXNNXXOc,,,;lxxk00Okdolllloddol::::clooolc:;;;:::;|\n |,,;;;'..,;;::::clodc.......:xO0KK00Odlc:;;:ldxooxOOkkxl;:okxdlllcccloolcc:;;;;;;|\n |'',,'','',,;clc;:ol'.. ....,lddxddoolllllc,,lkOxdooodxxddxxoooollllodxxxdlc:;;;;|\n |....''''',;;::;;::;..     ..,cllcclddddolc;;cd0XXOxl:coddkOkxdlccccldddoddlccc:;|\n |........,;,,,,'''''.       .':lodddxO00xlc::loxOO00Oddollldxkkdc:;;::;;;:::::;::|\n |........'...........        .':cclldk0K00OOo:c:cloxO0Oxdollllcc:,''''',,,,,,,,,,|\n |..'',;,,,..........          ..;:c:cdOKKXK0ocl:;;:;:ccccc::::;;;,......''''..'',|\n |;;;::::;'..........           ..:cclk00kxddoooc'.'..','.'',,,,,,'.....'''.......|\n |',;;;;;'.......'..              .:dkO00kxxdl:dxol:,,.',''...'.',;,'''...........|\n |,,;;,'............               .;okOkkkdlc:oxOx:'............',,''............|\n |.................                ..;ldxxxdoddddxxc........... ..''',,'..........|\n +--------------------------------------------------------------------------------+\n ")
	sys.stdout.write("Turn 5, enemy will get to objective in 1 turns. you are on " + player_infomation["player_position"] + ". please choose a direction: north, south, east, west, do nothing")
	answer = input("\n-")
	if answer == "north":
		if player_infomation["player_position"] == "A2":
			sys.stdout.write("you head north, you are now on -A2. you have reached the edge of the forest and found a clearing, stepping into the clearing you hear a loud horn. you left the forest and lost. The End \n")
			sys.stdout.write("+-----------------------------------------------------------------------------+ \n|------------------------#######----------------------------------------------| \n|---------------------------#----#----#-######--------------------------------| \n|---------------------------#----#----#-#-------------------------------------| \n|---------------------------#----######-#####---------------------------------| \n|---------------------------#----#----#-#-------------------------------------| \n|---------------------------#----#----#-#-------------------------------------| \n|---------------------------#----#----#-######--------------------------------| \n|-----------------------------------------------------------------------------| \n|-------------------------#######---------------------------------------------| \n|-------------------------#-------#----#-#####--------------------------------| \n|-------------------------#-------##---#-#----#-------------------------------| \n|-------------------------#####---#-#--#-#----#-------------------------------| \n|-------------------------#-------#--#-#-#----#-------------------------------| \n|-------------------------#-------#---##-#----#-------------------------------| \n|-------------------------#######-#----#-#####--------------------------------| \n+-----------------------------------------------------------------------------+ \n")
			exit()
			enemy["timer"] = "1"
	elif answer == "south":
		if player_infomation["player_position"] == "C2":
			sys.stdout.write("you head north, you are now on D2. you have reached the edge of the forest and found a clearing, stepping into the clearing you hear a loud horn. you left the forest and lost. The End \n")
			sys.stdout.write("+-----------------------------------------------------------------------------+ \n|------------------------#######----------------------------------------------| \n|---------------------------#----#----#-######--------------------------------| \n|---------------------------#----#----#-#-------------------------------------| \n|---------------------------#----######-#####---------------------------------| \n|---------------------------#----#----#-#-------------------------------------| \n|---------------------------#----#----#-#-------------------------------------| \n|---------------------------#----#----#-######--------------------------------| \n|-----------------------------------------------------------------------------| \n|-------------------------#######---------------------------------------------| \n|-------------------------#-------#----#-#####--------------------------------| \n|-------------------------#-------##---#-#----#-------------------------------| \n|-------------------------#####---#-#--#-#----#-------------------------------| \n|-------------------------#-------#--#-#-#----#-------------------------------| \n|-------------------------#-------#---##-#----#-------------------------------| \n|-------------------------#######-#----#-#####--------------------------------| \n+-----------------------------------------------------------------------------+ \n")
			exit()
			enemy["timer"] = "1"
	elif answer == "east":
		if player_infomation["player_position"] == "A3":
			sys.stdout.write("you head north, you are now on A4. you have reached the edge of the forest and found a clearing, stepping into the clearing you hear a loud horn. you left the forest and lost. The End \n")
			sys.stdout.write("+-----------------------------------------------------------------------------+ \n|------------------------#######----------------------------------------------| \n|---------------------------#----#----#-######--------------------------------| \n|---------------------------#----#----#-#-------------------------------------| \n|---------------------------#----######-#####---------------------------------| \n|---------------------------#----#----#-#-------------------------------------| \n|---------------------------#----#----#-#-------------------------------------| \n|---------------------------#----#----#-######--------------------------------| \n|-----------------------------------------------------------------------------| \n|-------------------------#######---------------------------------------------| \n|-------------------------#-------#----#-#####--------------------------------| \n|-------------------------#-------##---#-#----#-------------------------------| \n|-------------------------#####---#-#--#-#----#-------------------------------| \n|-------------------------#-------#--#-#-#----#-------------------------------| \n|-------------------------#-------#---##-#----#-------------------------------| \n|-------------------------#######-#----#-#####--------------------------------| \n+-----------------------------------------------------------------------------+ \n")
			exit()
			enemy["timer"] = "1"
		elif player_infomation["player_position"] == "B2":
			sys.stdout.write("you head east, you are now on B3.")
			enemy["timer"] = "1"
	elif answer == "west":
		if player_infomation["player_position"] == "A1":
			sys.stdout.write("you head north, you are now on A-0. you have reached the edge of the forest and found a clearing, stepping into the clearing you hear a loud horn. you left the forest and lost. The End \n")
			sys.stdout.write("+-----------------------------------------------------------------------------+ \n|------------------------#######----------------------------------------------| \n|---------------------------#----#----#-######--------------------------------| \n|---------------------------#----#----#-#-------------------------------------| \n|---------------------------#----######-#####---------------------------------| \n|---------------------------#----#----#-#-------------------------------------| \n|---------------------------#----#----#-#-------------------------------------| \n|---------------------------#----#----#-######--------------------------------| \n|-----------------------------------------------------------------------------| \n|-------------------------#######---------------------------------------------| \n|-------------------------#-------#----#-#####--------------------------------| \n|-------------------------#-------##---#-#----#-------------------------------| \n|-------------------------#####---#-#--#-#----#-------------------------------| \n|-------------------------#-------#--#-#-#----#-------------------------------| \n|-------------------------#-------#---##-#----#-------------------------------| \n|-------------------------#######-#----#-#####--------------------------------| \n+-----------------------------------------------------------------------------+ \n")
			exit()
			enemy["timer"] = "1"
	elif answer == "do nothing":
		sys.stdout.write("you stand still, trying to hide from everything that moves. \n")
		enemy["timer"] = "1"
	sys.stdout.write(forest2)
	sys.stdout.write("Turn 6, enemy will get to objective in 0 turns. you are on " + player_infomation["player_position"] + ". please choose a direction: north, south, east, west, do nothing\n")
	sys.stdout.write("+-----------------------------------------------------------------------------+ \n|------------------------#######----------------------------------------------| \n|---------------------------#----#----#-######--------------------------------| \n|---------------------------#----#----#-#-------------------------------------| \n|---------------------------#----######-#####---------------------------------| \n|---------------------------#----#----#-#-------------------------------------| \n|---------------------------#----#----#-#-------------------------------------| \n|---------------------------#----#----#-######--------------------------------| \n|-----------------------------------------------------------------------------| \n|-------------------------#######---------------------------------------------| \n|-------------------------#-------#----#-#####--------------------------------| \n|-------------------------#-------##---#-#----#-------------------------------| \n|-------------------------#####---#-#--#-#----#-------------------------------| \n|-------------------------#-------#--#-#-#----#-------------------------------| \n|-------------------------#-------#---##-#----#-------------------------------| \n|-------------------------#######-#----#-#####--------------------------------| \n+-----------------------------------------------------------------------------+ \n")
	sys.stdout.write("The " + enemy["enemy_type"] + " have reached the " + player_infomation["objective"] + ", you have not made it to the " + player_infomation["objective"] + " in time. The End \n")
main()