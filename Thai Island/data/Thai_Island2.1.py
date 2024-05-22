import time
import sys
import os
import pygame
from colorama import init, Fore, Back, Style

init()

menu_inicio_v=True
juego_v=True
playa_v=True
tribu_v=True
serpiente_v=True
selva_v=True
casa_v=True
pantano_v=True
tesoro_v=False 

colmillo_jefe_v=False
pollo_envenenado=False
veneno_v=False
cocodrilo_muerto=False

posibles_questions=["1", "2", "3", "4", "5", "6"]
objetos=[". Palo", ". Reloj", ". Cerillas"]
contador_objetos=0
nombre_personaje=str()
apellido_personaje=str()


# BARCO
mar_a=""
mar_b=" "
mar_c="@"



# MAPA

#Interfaz del mapa
palmera_unicode="\U0001f334"
cocodrilo_unicode="\U0001f40a"
serpiente_unicode="\U0001f40d"
tigre_unicode="\U0001f405"
tesoro_unicode="\u274C"
playa_unicode="\U0001f3dd\uFE0F"
cabaña_unicode="\U0001f6d6"
moai_unicode="\U0001f5ff"
fuego_unicode="\U0001f525"
casa_unicode="\U0001f3da\uFE0F"
arbol_unicode="\U0001f333"
personaje_unicode="\U0001f6b6"
mono_unicode="\U0001f412"

a="\033[0;31m" + "|" + "\033[0;32m"
b="\033[0;31m" + "-" + "\033[0;32m"
c="\033[0;31m" + "/" + "\033[0;32m"
d="\033[0;31m" + "\\" + "\033[0;32m"

#Variables de verificación del mapa
mapa_incorrecto=False
direction_v=False
direction=str()
vuelta1=True
mapa_v=True
mapa_obj=True


#Para mover de una posición a otra con pocas variables creadas
posicion=[ [False, 0], [False, 1], [False, 2], [False, 3], [False, 4], [False, 5]]

#Para saber que es lo que debemos preguntar
lugares=("1. Playa", "2. Aldea Indígena", "3. Selva", "4. Casa abandonada", "5. Pantano", "6. Tesoro")


# CANCIONES
pygame.mixer.init()

# Ruta relativa al archivo MP3 desde el script Python
ruta_archivo_mp3 = os.path.join('music', 'menu_inicio.mp3')

# Ruta absoluta del directorio donde se encuentra el script Python
ruta_script = os.path.dirname(os.path.abspath(sys.argv[0]))



song_menu_inicio=os.path.join(ruta_script, 'music', 'menu_inicio.mp3')
song_inicio_pirata=os.path.join(ruta_script, 'music', 'cancion_inicio_pirata.mp3')
song_playa=os.path.join(ruta_script, 'music', 'Playa.mp3')
song_tribu=os.path.join(ruta_script, 'music', 'cancion_tribu2.mp3')
song_selva=os.path.join(ruta_script, 'music', 'selva.mp3')
song_casa=os.path.join(ruta_script, 'music', 'casa.mp3')
song_pantano=os.path.join(ruta_script, 'music', 'pantano.mp3')
song_final=os.path.join(ruta_script, 'music', 'hfin_juego.mp3')
sonido_barco_olas=os.path.join(ruta_script, 'music', 'sonido_olas.mp3')
sonido_pum=os.path.join(ruta_script, 'music', 'sonido_pum.mp3')



# INTERFACES
menu_inicio=f"""






                                                                                        {Fore.LIGHTGREEN_EX} _____ _   _    _    ___     ___ ____  _        _    _   _ ____   
                                                                                        |_   _| | | |  / \  |_ _|   |_ _/ ___|| |      / \  | \ | |  _ \  
                                                                                          | | | |_| | / _ \  | |     | |\___ \| |     / _ \ |  \| | | | | 
                                                                                          | | |  _  |/ ___ \ | |     | | ___) | |___ / ___ \| |\  | |_| | 
                                                                                          |_| |_| |_/_/   \_\___|   |___|____/|_____/_/   \_\_| \_|____/ {Fore.RESET} 





                                                                                {Fore.LIGHTCYAN_EX}====================================================================================
                                                                                |                                                                                  |
                                                                                |{Fore.RESET}               _     ____  _             _                                        {Fore.LIGHTCYAN_EX}|{Fore.RESET}
                                                                                {Fore.LIGHTCYAN_EX}|{Fore.RESET}              / |   / ___|| |_ __ _ _ __| |_                                      {Fore.LIGHTCYAN_EX}|{Fore.RESET}                       ______ 
                                                                                {Fore.LIGHTCYAN_EX}|{Fore.RESET}              | |   \___ \| __/ _` | '__| __|                                     {Fore.LIGHTCYAN_EX}|{Fore.RESET}                   _.-':::::::`.               
          .=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-.                    {Fore.LIGHTCYAN_EX}|{Fore.RESET}              | |_   ___) | || (_| | |  | |_                                      {Fore.LIGHTCYAN_EX}|{Fore.RESET}                   \::::::::::::`.-._             
          |                     ______                     |                    {Fore.LIGHTCYAN_EX}|{Fore.RESET}              |_(_) |____/ \__\__,_|_|   \__|                                     {Fore.LIGHTCYAN_EX}|{Fore.RESET}                    \:::''   `::::`-.`. 
          |                  .-"      "-.                  |                    {Fore.LIGHTCYAN_EX}|{Fore.RESET}                                                                                  {Fore.LIGHTCYAN_EX}|{Fore.RESET}{Fore.RESET}                     \         `:::::`.\\
          |                 /            \                 |                    {Fore.LIGHTCYAN_EX}|{Fore.RESET}                                                                                  {Fore.LIGHTCYAN_EX}|{Fore.RESET}                      \          `-::::`: 
          |     _          |              |          _     |                    {Fore.LIGHTCYAN_EX}|{Fore.RESET}                                                                                  {Fore.LIGHTCYAN_EX}|{Fore.RESET}                       \______       `:::`. 
          |    ( \         |,  .-.  .-.  ,|         / )    |                    {Fore.LIGHTCYAN_EX}|{Fore.RESET}               ____      _   _                 _                _                 {Fore.LIGHTCYAN_EX}|{Fore.RESET}                       .|_.-'__`._     `:::\ 
          |     > "=._     | )(__/  \__)( |     _.=" <     |                    {Fore.LIGHTCYAN_EX}|{Fore.RESET}              |___ \    | | | | _____      __ | |_ ___    _ __ | | __ _ _   _     {Fore.LIGHTCYAN_EX}|{Fore.RESET}                      ,'`|:::|  )/`.     \:::
          |    (_/"=._"=._ |/     /\     \| _.="_.="\_)    |                    {Fore.LIGHTCYAN_EX}|{Fore.RESET}                __) |   | |_| |/ _ \ \ /\ / / | __/ _ \  | '_ \| |/ _` | | | |    {Fore.LIGHTCYAN_EX}|{Fore.RESET}                     /. -.`--'  : /.\     ::|
          |           "=._"(_     ^^     _)"_.="           |                    {Fore.LIGHTCYAN_EX}|{Fore.RESET}               / __/ _  |  _  | (_) \ V  V /  | || (_) | | |_) | | (_| | |_| |    {Fore.LIGHTCYAN_EX}|{Fore.RESET}                     `-,-'  _,'/| \|\\    |:|
          |               "=\__|IIIIII|__/="               |                    {Fore.LIGHTCYAN_EX}|{Fore.RESET}              |_____(_) |_| |_|\___/ \_/\_/    \__\___/  | .__/|_|\__,_|\__, |    {Fore.LIGHTCYAN_EX}|{Fore.RESET}                      ,'`::.    |/>`;'\   |:|
          |              _.="| \IIIIII/ |"=._              |                    {Fore.LIGHTCYAN_EX}|{Fore.RESET}                                                         |_|            |___/     {Fore.LIGHTCYAN_EX}|{Fore.RESET}                      \.:\ ::_:_:_`-','  `-:|
          |    _     _.="_.="\          /"=._"=._     _    |                    {Fore.LIGHTCYAN_EX}|{Fore.RESET}                                                                                  {Fore.LIGHTCYAN_EX}|{Fore.RESET}                       `:\\|         
          |   ( \_.="_.="     `--------`     "=._"=._/ )   |                    {Fore.LIGHTCYAN_EX}|{Fore.RESET}                                                                                  {Fore.LIGHTCYAN_EX}|{Fore.RESET}                          )`__...---'
          |    > _.="                            "=._ <    |                    {Fore.LIGHTCYAN_EX}|{Fore.RESET}               _____    _____      _ _                                            {Fore.LIGHTCYAN_EX}|{Fore.RESET}
          |   (_/                                    \_)   |                    {Fore.LIGHTCYAN_EX}|{Fore.RESET}              |___ /   | ____|_  _(_) |_                                          {Fore.LIGHTCYAN_EX}|{Fore.RESET}
          |                                                |                    {Fore.LIGHTCYAN_EX}|{Fore.RESET}                |_ \   |  _| \ \/ / | __|                                         {Fore.LIGHTCYAN_EX}|{Fore.RESET}
          '-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-='                    {Fore.LIGHTCYAN_EX}|{Fore.RESET}               ___) |  | |___ >  <| | |_                                          {Fore.LIGHTCYAN_EX}|{Fore.RESET}
                                                                                {Fore.LIGHTCYAN_EX}|{Fore.RESET}              |____(_) |_____/_/\_\_|\__|                                         {Fore.LIGHTCYAN_EX}|{Fore.RESET}
                                                                                {Fore.LIGHTCYAN_EX}|                                                                                  | 
                                                                                |__________________________________________________________________________________|
                                                                                
                                                                                """




inventario_intf=(f""" {Fore.LIGHTWHITE_EX}
_____________________________________________________________________________________________________________________________________
|                                                                                                                                   |
|                           ___                 _            _          _        ___  _     _     _                                 |
|                          |_ _|_ ___ _____ _ _| |_ __ _ _ _(_)___   __| |___   / _ \| |__ (_)___| |_ ___ ___                       |
|                           | || ' \ V / -_) ' \  _/ _` | '_| / _ \ / _` / -_) | (_) | '_ \| / -_)  _/ _ (_-<                       |
|                          |___|_||_\_/\___|_||_\__\__,_|_| |_\___/ \__,_\___|  \___/|_.__// \___|\__\___/__/                       |
|                                                                                         |__/                                      |
|___________________________________________________________________________________________________________________________________|
            
            """)

usar_intf=(f""" {Fore.LIGHTWHITE_EX}
_____________________________________________________________________________________________________________________________________
|                                                                                                                                   |
|                                                               _   _                                                               |
|                                                              | | | |___ __ _ _ _                                                  |
|                                                              | |_| (_-</ _` | '_|                                                 |
|                                                               \___//__/\__,_|_|                                                   |
|                                                                                                                                   |
|___________________________________________________________________________________________________________________________________|
            
{Fore.LIGHTRED_EX}Formula= 'objeto' + 'con' + 'objeto, animal o persona'{Fore.RESET}            
""")


coger_intf=(f""" {Fore.LIGHTWHITE_EX}
_____________________________________________________________________________________________________________________________________
|                                                                                                                                   |
|                                                             __                                                                    |
|                                                           / __|___  __ _ ___ _ _                                                  |
|                                                          | (__/ _ \/ _` / -_) '_|                                                 |
|                                                           \___\___/\__, \___|_|                                                   |
|                                                                    |___/                                                          |
|                                                                                                                                   |
|___________________________________________________________________________________________________________________________________|
            
            """)


dar_intf=(f""" {Fore.LIGHTWHITE_EX}
_____________________________________________________________________________________________________________________________________
|                                                                                                                                   |
|                                                            ___                                                                    |
|                                                           |   \ __ _ _ _                                                          |
|                                                           | |) / _` | '_|                                                         |
|                                                           |___/\__,_|_|                                                           |
|                                                                                                                                   |
|                                                                                                                                   |
|___________________________________________________________________________________________________________________________________|
            
{Fore.LIGHTRED_EX}Formula= 'objeto' + 'a' + 'animal o persona'{Fore.RESET}            
""")


acciones=(f"""{Fore.LIGHTWHITE_EX}
_____________________________________________________________________________________________________________________________________
|                                                                                                                                   |
|          Elige la accion que quieres realizar                                                                                     |
|          _      ____                                                          ____      _   _                                     |
|         / |    / ___|___   __ _  ___ _ __                                    |___ \    | | | |___  __ _ _ __                      |
|         | |   | |   / _ \ / _` |/ _ \ '__|                                     __) |   | | | / __|/ _` | '__|                     |
|         | |_  | |__| (_) | (_| |  __/ |                                       / __/ _  | |_| \__ \ (_| | |                        |
|         |_( )  \____\___/ \__, |\___|_|                                      |_____(_) _\___/|___/\__,_|_|                        |
|                            |__ /                                                                                                  |
|          _____    ____                                 _  _     _      _           ___                      _             _       |
|         |___ /   |  _ \  ____ __ _                    | || |    \ \   / /__ _ __  |_ _|_ ____   _____ _ __ | |_ __ _ _ __(_) ___  |
|           |_ \   | | | |/ _` | '__|                   | || |_    \ \ / / _ \ '__|  | || '_ \ \ / / _ \ '_ \| __/ _` | '__| |/ _ \ |
|          ___) |  | |_| | (_| | |                      |__   _|    \ V /  __/ |     | || | | \ V /  __/ | | | || (_| | |  | | (_) ||
|         |____(_) |____/ \__,_|_|                         |_|(_)    \_/ \___|_|    |___|_| |_|\_/ \___|_| |_|\__\__,_|_|  |_|\___/ |  
|                                                                                                                                   |""")


playa=(f"""                          {Fore.GREEN}#####                                                                                                         
                       #######                                                                                                              
            ######    ########       #####                                                                                                  
        ###########/#####\#####  #############                                                                                              
    ############/##########--#####################
  ####         ######################          #####                                                                                        
 ##          ####      ##########/@@              ###
#          ####        ,-.##/`.#\#####               ##
          ###        {Fore.YELLOW} /  |./  |,-. {Fore.GREEN}####                 #
         ##           {Fore.YELLOW}\_,'\_,'|  \  {Fore.GREEN}###
         #             {Fore.YELLOW}\_{Fore.LIGHTBLACK_EX}$$$$${Fore.YELLOW}`._/   {Fore.GREEN}##   
                          {Fore.LIGHTBLACK_EX}$$$$${Fore.YELLOW}_/     {Fore.GREEN}# {Fore.LIGHTBLACK_EX}    
                          $$$$$        
                          $$$$$
                          $$$$$
                          $$$$$
                          $$$$$
                         $$$$$
                         $$$$$
                         $$$$$
                         $$$$$        ___
                         $$$$$    _.-'   `-._
                        $$$$$   ,'           `.
                        $$$$$  /               '                                                                                                              .                                                                     .
~~~~~~~~~~~~~~~~~~~~~~~$$$$$~~~'~~~~~~~~~~~~~~~~`~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~{Back.BLACK}                                                                     
{Back.BLUE}   ~      ~  ~    ~  ~ {Back.BLACK}{Fore.LIGHTBLACK_EX}$$$$${Back.BLUE}  ~   ~       ~          ~                                                                                {Back.BLACK}
{Back.BLUE}       ~               {Back.BLACK}{Fore.LIGHTBLACK_EX}$$$$${Back.BLUE}     ~    ~          ~                                                                                    {Back.BLACK}
{Back.BLUE}  ~            ~    ~  {Back.BLACK}{Fore.LIGHTBLACK_EX}$$$$${Back.BLUE}~                     ~        ~                                                                          {Back.BLACK}
{Back.BLUE}                       {Back.BLACK}{Fore.LIGHTBLACK_EX}$$$$${Back.BLUE}                                                                                                          {Back.BLACK}
{Back.LIGHTYELLOW_EX}                       {Back.BLACK}{Fore.LIGHTBLACK_EX}$$$$${Back.LIGHTYELLOW_EX}                                                                                                          {Back.BLACK}
{Back.LIGHTYELLOW_EX}                       {Back.BLACK}{Fore.LIGHTBLACK_EX}$$$$${Back.LIGHTYELLOW_EX}                                                                                                          {Back.BLACK}
{Back.LIGHTYELLOW_EX}                       {Back.BLACK}{Fore.LIGHTBLACK_EX}$$$$${Back.LIGHTYELLOW_EX}                                                                                                          {Back.BLACK}
{Back.LIGHTYELLOW_EX}                       {Back.BLACK}{Fore.LIGHTBLACK_EX}$$$$${Back.LIGHTYELLOW_EX}                                                                                                          {Back.BLACK}
{Back.LIGHTYELLOW_EX}                      {Back.BLACK}{Fore.LIGHTBLACK_EX}$$$$$$${Back.LIGHTYELLOW_EX}                                                                                                         {Back.BLACK}
{Back.LIGHTYELLOW_EX}                      {Back.BLACK}{Fore.LIGHTBLACK_EX}$$$$$$${Back.LIGHTYELLOW_EX}                                                                                                         {Back.BLACK}
{Back.LIGHTYELLOW_EX}                     {Back.BLACK}{Fore.LIGHTBLACK_EX}$$$$$$$$${Back.LIGHTYELLOW_EX}                                                                                                        {Back.BLACK}
{Back.LIGHTYELLOW_EX}                     {Back.BLACK}{Fore.LIGHTBLACK_EX}$$$$$$$$${Back.BLACK}
""")



tribu=f"""{Fore.RED}                                                                                                                                                                         @                
                                                                                                                                                                                       ,   @            
                                                                                                                                                                                    ., @  * @       
              @@@              (@@                             @@&              @@@                                                                       @@@&@                      @..,&#@, @@ .      
              @@@     @@@@@    @&@            @@@@@            @@@    @@@@@     @@&                                                                      @@@@@@@.              @   ,(/&@@@@@%@@@%&@      
               @@   .@@@@@@@   @@@           @@@@@@@           @@@   @@@@@@@*   @@.                                                                        @@@&                  @ @@@@@@@@@@@@@@@@&  @   
               @&@@.  @@@@.  @@@(#            /@@@(            (&@@@   @@@@  .@@@@                                                            &@@@     @@@@@@@@@@@              @@@@@@@#@@@@@@@@@@@@@@       
                  @@&*@@@@@ @@        @ @@@@@ @@@@@ @@@@@ @        @@ @@@@@/#@&                                                              @@@@@@@  @@@@@@@@@@@@@@         @@@@@@@@@@@#*   ,@@@@@%@@@@    
                    @*@@@@@@@          @ @  @ @@@@@ @  @.@          &/@@@@@*@                                                                 @@@@@  @@@@@@@@@@@@ @@@      %@@@@@@#@@&@@@&*,.,/&@@@@@@@@@@     
                    @@@@@@@@@            @@@@@@@@@@@@@@@            &@@@@@@@@                                                               @@@@@@@@@#@ @@@@@@@@@ @@@     @,@ @.@*@ @@@@@@@@@@@@@ @%@@@*@,@/     
                     #@@@@@                  *@@@@@*                 .&@@@@#                    @@                                        @@@@@@@@@@@@* @@@@@@@@@ @@@   @@@/@.@*@.@@@@@@@@@@@@@@@@@ @ @ @.@ @    
                    @@@@@@@@@               @@@@@@@@@               &@@@@@@@@                      @@.                                    @@.@@@@@@@ @@ @@@,  @@@ @@@  @ @ @ @ @ @@@@@@@@@@@@@@@@@@@ @ @ @,@ @    
               ,@/@@@@@  ,@@@@ @%       &@,@@@@   @@@@*@&       #@ @@@@/  @@@@@/@,                    .@@                                (@%.@@@@@@@ @@ @@@@  @@@  .  @ @ @ @ @ @@@@@@@@@@@@@@@@@@@@@ @ @ #@@%@      
             @@@@@#@@      (@.@@@@@  *@@@@@(@,     .@,@@@@@.  @@@@@ @/      &@&@@@@@                      @@                             /@&.@@  @@@ @@ @@@@*@@@@      @   @ @ @@@@@@@@@@@@@@@@@@@@@@@ @ @   %&    
             (%@@%             @@@@   @@@@             @@@@   @@@%.            #@@@%                         ,@&                            .@@@ @@@    @@@@*@@@@  .      &/   @@@@@@@@@@@@@@@@@@@@@@/    @   #    
              , #@             @, @   % (@             @( #   % ,%             @& *                             .@@ .                                                                      
                                                                                                                    @@*                                                                                                    @@.                                                            
                                           &&&     .                                                                     ,@@@@
              .                            %&#                                                                         @@@@@@,@@. 
                                  .&    ,&&&&&              .                                                        ,@@@@@      %@#   
                                &&&   &&&&&&&    &                                                                   @@@@(           @@
                              /&&&&  &&&&&&&*    &&                                                                 %@@@@               @@,
                              &&&&&&&&&&&&&&    &&&%      .                                                          @@@@%        (@@@@@,  .@@
                 .            &&&&&&&&&&&&&&  &&&&&,                                                                 .@@@@@#    @@@@*  %@@%    @@,   
                               &&&&&&&&&&&&&&&&&&&   &                                                                  @@@@@@@@@@@@@@@@@@&.      ,@@  
                        &&   &&&&&& &&&&&&&&&&       #&                                                                 @@@@@@@/@@@@@@@@@@@           @@
                         &&&&&#&&&&&&{Back.YELLOW}     {Back.RESET}{Fore.RED}&& &&&&&   &&                                                                @@@@@@@@@*@@@@@@@@,              @@@@@@*
                         &&&&&&&&&&&{Back.YELLOW}          {Back.RESET}{Fore.RED}&&&&&&&&&*                                                              #@@@@@@@@@@@@@@@@@@@@@/             @%@@@@*            
                          &&&&&&&{Back.YELLOW}            {Back.RESET}{Fore.RED}&&&&&&&&&                                                                @@@@@@@@@@@@@@@    &@@@@@                .&@            
                          &&&&&&{Back.YELLOW}              {Back.RESET}{Fore.RED}&& &&&&&%                                                               @@@@@@@@@@@@@@@    &@@@@@                .&@ 
                           (%&&&{Back.YELLOW}                 {Back.RESET}{Fore.RED}&&&&,                                                                @@@@@@@@@@@@@,       @@@@@@
                             %&&&{Back.YELLOW}               {Back.RESET}{Fore.RED}&&&/                                                                 ,@@@@@@@@@@@@*          @@@@@,  
                          /&&&&%(&&{Back.YELLOW}          {Back.RESET}{Fore.RED}/&&(&&                                                                  *@@@@@@@@@@@@             @@&@@   
                         .&&&&&&&&&&&#{Back.YELLOW}    {Back.RESET}{Fore.RED}.#&&&&&                                                                    #@@@@@    @@@               @@@@@   
                          &&&&&&(,&&&&&&&&&&&&&&&.                                                                   @@@@@&    @@@@@*            .@@(  
                           .&&&&&&&&&&&&&&&&&&&&&&& &                                                               (@@@@@@    @@@@@@@  
                      &&&&&&&&&&&&&&&&&&&&&&&%/#&&&&&&&&&&&                                                         @@@@@@@     @@@@@@@( 
                     & ( # &&&&&&&&&&&&&&&.&&&&&&&&&&& * ( &,                                                      @@@@@@@       @@@@@@@   
                                                                                                                 ,@@@@@@@         @@@@@@@"""

tribu_anim=f"""{Fore.RED}                                                                                                                                                                             @                            
                                                                                                                                                                                        ,   @                           
                                                                                                                                                                                      ., @  * @                        
                                     @@@              (@@                                                                                                 @@@&@                      @..,&#@, @@ .                      
                     @@@@@           @@@     @@@@@    @&@              @@@@@                                                                             @@@@@@@.              @   ,(/&@@@@@%@@@%&@                    
                    @@@@@@@           @@   .@@@@@@@   @@@             @@@@@@@                                                                              @@@&                  @ @@@@@@@@@@@@@@@@&  @                
                     /@@@(            @&@@.  @@@@.  @@@(#              /@@@(                                                                  &@@@     @@@@@@@@@@@              @@@@@@@#@@@@@@@@@@@@@@                 
             @ @@@@@ @@@@@ @@@@@ @       @@&*@@@@@ @@          @ @@@@@ @@@@@ @@@@@ @                                                         @@@@@@@  @@@@@@@@@@@@@@         @@@@@@@@@@@#*   ,@@@@@%@@@@               
              @ @  @ @@@@@ @  @.@          @*@@@@@@@            @ @  @ @@@@@ @  @.@                                                           @@@@@  @@@@@@@@@@@@ @@@      %@@@@@@#@@&@@@&*,.,/&@@@@@@@@@@             
                @@@@@@@@@@@@@@@            @@@@@@@@@              @@@@@@@@@@@@@@@                                                           @@@@@@@@@#@ @@@@@@@@@ @@@     @,@ @.@*@ @@@@@@@@@@@@@ @%@@@*@,@/           
                    *@@@@@*                 #@@@@@                    *@@@@@*                   @@                                        @@@@@@@@@@@@* @@@@@@@@@ @@@   @@@/@.@*@.@@@@@@@@@@@@@@@@@ @ @ @.@ @           
                   @@@@@@@@@               @@@@@@@@@                 @@@@@@@@@                     @@.                                    @@.@@@@@@@ @@ @@@,  @@@ @@@  @ @ @ @ @ @@@@@@@@@@@@@@@@@@@ @ @ @,@ @         
               &@,@@@@   @@@@*@&       ,@/@@@@@  ,@@@@ @%        &@,@@@@   @@@@*@&                    .@@                                (@%.@@@@@@@ @@ @@@@  @@@  .  @ @ @ @ @ @@@@@@@@@@@@@@@@@@@@@ @ @ #@@%@        
            *@@@@@(@,     .@,@@@@@.  @@@@@#@@      (@.@@@@@   *@@@@@(@,     .@,@@@@@.                     @@                             /@&.@@  @@@ @@ @@@@*@@@@      @   @ @ @@@@@@@@@@@@@@@@@@@@@@@ @ @   %&        
             @@@@             @@@@    (%@@%             @@@@   @@@@             @@@@                         ,@&                            .@@@ @@@    @@@@*@@@@  .      &/   @@@@@@@@@@@@@@@@@@@@@@/    @   #        
             % (@             @( #     , #@             @, @   % (@             @( #                            .@@ .                                                                                                  
                                                                                                                    @@*                                                                                                    @@.                                                                                              
                                           &&&                                                                           ,@@@@                                                                                          
                                           %&#                                                                         @@@@@@,@@.                                                                                       
                                  .&    ,&&&&&                                                                       ,@@@@@      %@#                                                                                    
                                &&&   &&&&&&&   &                                                                    @@@@(           @@                                                                                 
                              /&&&&  &&&&&&&*   &&                                                                  %@@@@               @@,                                                                             
                              &&&&&&&&&&&&&&   &&&%                                                                  @@@@%        (@@@@@,  .@@                                                                          
                              &&&&&&&&&&&&&& &&&&&,                                                                  .@@@@@#    @@@@*  %@@%    @@,                                                                      
                               &&&&&&&&&&&&&&&&&&&   &                                                                  @@@@@@@@@@@@@@@@@@&.      ,@@                                                                   
                          &&    &&&&&& &&&&&&&&&&    #&                                                                 @@@@@@@/@@@@@@@@@@@           @@                                                                
                         &&&&&#&&&&&&    && &&&&&    &&                                                                @@@@@@@@@*@@@@@@@@,              @@@@@@*                                                         
                         &&&&&&&&&&&     &&   &&&&&&&&&*                                                              #@@@@@@@@@@@@@@@@@@@@@/             @%@@@@*                                                       
                          &&&&&&&(      &*    &&&&&&&&&                                                               @@@@@@@@@@@@@@@    &@@@@@                .&@                                                      
                          &&&&&&              && &&&&&%                                                               @@@@@@@@@@@@@@@    &@@@@@                .&@                                                      
                           (%&&&                 &&&&,                                                                @@@@@@@@@@@@@,       @@@@@@                                                                       
                             %&&&               &&&/                                                                 ,@@@@@@@@@@@@*          @@@@@,                                                                     
                          /&&&&%(&&          /&&(&&                                                                  *@@@@@@@@@@@@             @@&@@                                                                    
                         .&&&&&&&&&&&#    .#&&&&&                                                                    #@@@@@    @@@              @@@@@                                                                   
                          &&&&&&(,&&&&&&&&&&&&&&&.                                                                   @@@@@&    @@@@@*            .@@(                                                                   
                           .&&&&&&&&&&&&&&&&&&&&&&& &                                                               (@@@@@@    @@@@@@@                                                                                  
                      &&&&&&&&&&&&&&&&&&&&&&&%/#&&&&&&&&&&&                                                         @@@@@@@     @@@@@@@(                                                                                
                     & ( # &&&&&&&&&&&&&&&.&&&&&&&&&&& * ( &,                                                      @@@@@@@       @@@@@@@                                                                                
                                                                                                                 ,@@@@@@@         @@@@@@@"""

tribu_menu=(f"""{Fore.RED}
:-..                        .:. .                         . :-                         .....        
.                          ....                         .: .                         ...:.          
    .              #*-.=@=.-=#%%@@@@@@@@@@@@@@@@@@@@@.  -..   ..                     ...    .       
      .         .+%.                               %@@.         .                 .          .     
       ..     @         {Fore.LIGHTWHITE_EX}No sé si te has dado cuenta,{Fore.RED}  @@.         .              .              .   
          .   @    {Fore.LIGHTWHITE_EX}pero somos adoradores del tiempo,{Fore.RED}    @@+         .          .                  . 
           .  @   {Fore.LIGHTWHITE_EX}y es en lo único en lo que creemos.{Fore.RED}     @*          .       .                     
             .@@      {Fore.LIGHTWHITE_EX}Piensa en algo, quizás puedas{Fore.RED}       @%                .                       
             ++:   {Fore.LIGHTWHITE_EX}demostrarnos tu confianza, de alguna{Fore.RED}   @#             ...                        
             **   {Fore.LIGHTWHITE_EX}manera, al igual que hizo el anterior{Fore.RED}   @=                                        
           . %*   {Fore.LIGHTWHITE_EX}forastero.{Fore.RED}                              @@-          .       .                    .
          .  %=                                           @         .          .                  . 
       ..    %+                                           @=                     .              .   
      .      -@                                          -@      .                 .          .     
  ...        .@@                                       @@@@ ....                     .    .-.       
 ....           .@                                    @:    .....                         :-:-       
...               @=                                @.    . .                          -...         
..                .@@@@@@@%+=-......@@@@@@@@@@@@@@@@@   ....                         --:-.          
    .                      -:.@.....@:                  ..     .  @.                  ..    .       
      .                 .     .@....**                           .=@               :          .     
        .              .       .%@...@             ..  ..         .@@=.          .              .   
          .         .             @%.#+.         =@@%....@@+      :@::%@@      .                  : 
           ..      .               .@@@. .     :%:..........%@.   %%:@:@*..@@*.                    .
                                      @@.     @@..............@%   .@@@@::@-@ .                     
              -..                       .  ..+@................+@   .@%*@==-@@.                     
             .                            . .@*.................@=   *@*@.  .                       
           .       .                        -@...................@    @@=@   ..                    .
         .           :          %@@@@@.     *%..#.@..............@  .  @=%+     .                   
       ..             ..        @@..@@:   .@.@................:.@@:     @-@      .              .   
                         .    .@*...#@@.     @@@@+.   :*@@.....#-@-     .@-+@.@-   .                
  -:.                     .    ..:@.@@                  .#@..--..@:     %#.@@@.@.    .    ...       
:-:-.                        ....:@.=@      *@@@@@@@.@@#..@-.-...@.     .@.#@=.@.       .....       
...                         ....  @..@     .@*=::........:-:.....@    . @..@@=@=       ....         
-                         ....    :@.=@.    %@..........-:......*@.   .@:.@.@*=@.   .....           
    .                      ..     .:@.+@    .@-......:--+#%@@#++@@   *@.+@. .@-+@.    ..            
      ..                :          ..@@.@@.  @@#+:%#%@++@*=:....@+ .@#.@*    .@-#@.           ..    
        .             .                %@+=@@@....*@.+..@.......:@@:.@@.      -@-@:             .   
          .         .                  . .@@=.....@@..@@@+........#@%.         +@-@.              . 
            .     .                      .  @-.......%@*=-:......@.    .     .  #@-@.               
                                            %+.......%:+%........@               %@-@               
              ..                           .+@........@:%.......:@       ...      @@-@.             
             .                              .@..........-.......*@.     .   .      @@#*             
                                                     {Fore.RESET}jefe                """)


tribu_menu2=(f"""{Fore.RED}
:-..                        .:. .                         . :-                         .....        
.                          ....                         .: .                         ...:.          
    .              #*-.=@=.-=#%%@@@@@@@@@@@@@@@@@@@@@.  -..   ..                     ...    .       
      .         .+%.                               %@@.         .                 .          .     
       ..     @   {Fore.LIGHTWHITE_EX}¡Buenas forastero!, Me sorprende{Fore.RED}  @@.         .              .              .   
          .   @   {Fore.LIGHTWHITE_EX}que sigas vivo y todavía no te{Fore.RED}     @@+         .          .                  . 
           .  @    {Fore.LIGHTWHITE_EX}haya comido el monstruo. {Fore.RED}         @*          .       .                     
             .@@    {Fore.LIGHTWHITE_EX}El día que esa bestia muera{Fore.RED}      @%                .                       
             ++:   {Fore.LIGHTWHITE_EX}podremos dormir tranquilos por{Fore.RED}    @#             ...                        
             **   {Fore.LIGHTWHITE_EX}las noches. En nuestra cultura{Fore.RED}      @=                                        
           . %*{Fore.LIGHTWHITE_EX}el vaiente que sea capaz de vencerlo,{Fore.RED}  @@-          .       .                    .
          .  %=   {Fore.LIGHTWHITE_EX}será recompensado con una ofrenda.{Fore.RED}  @         .          .                  . 
       ..    %+ {Fore.LIGHTWHITE_EX}Esto también va por ti forastero,{Fore.RED}     @=                     .              .   
      .      -@  {Fore.LIGHTWHITE_EX}si consigues acabar con la bestia,{Fore.RED}  -@      .                 .          .     
  ...        .@@    {Fore.LIGHTWHITE_EX}y nos traer una prueba, serás {Fore.RED} @@@@ ....                     .    .-.       
 ....           .@    {Fore.LIGHTWHITE_EX}recompensado{Fore.RED}                 @:    .....                         :-:-       
...               @=                                @.    . .                          -...         
..                .@@@@@@@%+=-......@@@@@@@@@@@@@@@@@   ....                         --:-.          
    .                      -:.@.....@:                  ..     .  @.                  ..    .       
      .                 .     .@....**                           .=@               :          .     
        .              .       .%@...@             ..  ..         .@@=.          .              .   
          .         .             @%.#+.         =@@%....@@+      :@::%@@      .                  : 
           ..      .               .@@@. .     :%:..........%@.   %%:@:@*..@@*.                    .
                                      @@.     @@..............@%   .@@@@::@-@ .                     
              -..                       .  ..+@................+@   .@%*@==-@@.                     
             .                            . .@*.................@=   *@*@.  .                       
           .       .                        -@...................@    @@=@   ..                    .
         .           :          %@@@@@.     *%..#.@..............@  .  @=%+     .                   
       ..             ..        @@..@@:   .@.@................:.@@:     @-@      .              .   
                         .    .@*...#@@.     @@@@+.   :*@@.....#-@-     .@-+@.@-   .                
  -:.                     .    ..:@.@@                  .#@..--..@:     %#.@@@.@.    .    ...       
:-:-.                        ....:@.=@      *@@@@@@@.@@#..@-.-...@.     .@.#@=.@.       .....       
...                         ....  @..@     .@*=::........:-:.....@    . @..@@=@=       ....         
-                         ....    :@.=@.    %@..........-:......*@.   .@:.@.@*=@.   .....           
    .                      ..     .:@.+@    .@-......:--+#%@@#++@@   *@.+@. .@-+@.    ..            
      ..                :          ..@@.@@.  @@#+:%#%@++@*=:....@+ .@#.@*    .@-#@.           ..    
        .             .                %@+=@@@....*@.+..@.......:@@:.@@.      -@-@:             .   
          .         .                  . .@@=.....@@..@@@+........#@%.         +@-@.              . 
            .     .                      .  @-.......%@*=-:......@.    .     .  #@-@.               
                                            %+.......%:+%........@               %@-@               
              ..                           .+@........@:%.......:@       ...      @@-@.             
             .                              .@..........-.......*@.     .   .      @@#*             
                                                     {Fore.RESET}jefe                """)



tribu_menu3=(f"""{Fore.RED}
:-..                        .:. .                         . :-                         .....        
.                          ....                         .: .                         ...:.          
    .              #*-.=@=.-=#%%@@@@@@@@@@@@@@@@@@@@@.  -..   ..                     ...    .       
      .         .+%.                               %@@.         .                 .          .     
       ..     @        {Fore.LIGHTWHITE_EX}¡Este colmillo tiene que{Fore.RED}     @@.         .              .              .   
          .   @     {Fore.LIGHTWHITE_EX} ser de la bestia!. No puedo{Fore.RED}     @@+         .          .                  . 
           .  @    {Fore.LIGHTWHITE_EX} creer que hayas acabado con él.{Fore.RED}   @*          .       .                     
             .@@ {Fore.LIGHTWHITE_EX}Como te prometí, serás recompensado,{Fore.RED}  @%                .                       
             ++:   {Fore.LIGHTWHITE_EX}aquí tienes la llave que tanto{Fore.RED}      @#             ...                        
             **  {Fore.LIGHTWHITE_EX}ansiaba el otro forastero encontrar{Fore.RED}   @=                                        
           . %*  {Fore.LIGHTWHITE_EX}supongo que estos objetos serán muy{Fore.RED}   @@-          .       .                    .
          .  %=        {Fore.LIGHTWHITE_EX}valiosos en vuestra cultura.{Fore.RED}    @         .          .                  . 
       ..    %+                                        @=                     .              .   
      .      -@        {Fore.LIGHTWHITE_EX}Espero que la disfrutes.{Fore.RED}       -@      .                 .          .     
  ...        .@@                                     @@@@ ....                     .    .-.       
 ....           .@                                   @:    .....                         :-:-       
...               @=                                @.    . .                          -...         
..                .@@@@@@@%+=-......@@@@@@@@@@@@@@@@@   ....                         --:-.          
    .                      -:.@.....@:                  ..     .  @.                  ..    .       
      .                 .     .@....**                           .=@               :          .     
        .              .       .%@...@             ..  ..         .@@=.          .              .   
          .         .             @%.#+.         =@@%....@@+      :@::%@@      .                  : 
           ..      .               .@@@. .     :%:..........%@.   %%:@:@*..@@*.                    .
                                      @@.     @@..............@%   .@@@@::@-@ .                     
              -..                       .  ..+@................+@   .@%*@==-@@.                     
             .                            . .@*.................@=   *@*@.  .                       
           .       .                        -@...................@    @@=@   ..                    .
         .           :          %@@@@@.     *%..#.@..............@  .  @=%+     .                   
       ..             ..        @@..@@:   .@.@................:.@@:     @-@      .              .   
                         .    .@*...#@@.     @@@@+.   :*@@.....#-@-     .@-+@.@-   .                
  -:.                     .    ..:@.@@                  .#@..--..@:     %#.@@@.@.    .    ...       
:-:-.                        ....:@.=@      *@@@@@@@.@@#..@-.-...@.     .@.#@=.@.       .....       
...                         ....  @..@     .@*=::........:-:.....@    . @..@@=@=       ....         
-                         ....    :@.=@.    %@..........-:......*@.   .@:.@.@*=@.   .....           
    .                      ..     .:@.+@    .@-......:--+#%@@#++@@   *@.+@. .@-+@.    ..            
      ..                :          ..@@.@@.  @@#+:%#%@++@*=:....@+ .@#.@*    .@-#@.           ..    
        .             .                %@+=@@@....*@.+..@.......:@@:.@@.      -@-@:             .   
          .         .                  . .@@=.....@@..@@@+........#@%.         +@-@.              . 
            .     .                      .  @-.......%@*=-:......@.    .     .  #@-@.               
                                            %+.......%:+%........@               %@-@               
              ..                           .+@........@:%.......:@       ...      @@-@.             
             .                              .@..........-.......*@.     .   .      @@#*             
                                                     {Fore.RESET}jefe                """)





tribu_menu4=(f"""{Fore.RED}
:-..                        .:. .                         . :-                         .....        
.                          ....                         .: .                         ...:.          
    .              #*-.=@=.-=#%%@@@@@@@@@@@@@@@@@@@@@.  -..   ..                     ...    .       
      .         .+%.                                 %@@.         .                 .          .     
       ..     @                                       @@.         .              .              .   
          .   @                                       @@+         .          .                  . 
           .  @            {Fore.LIGHTWHITE_EX}Buenas forastero,{Fore.RED}           @*          .       .                     
             .@@                                       @%                .                       
             ++:           {Fore.LIGHTWHITE_EX}¿Qué tal va todo?{Fore.RED}            @#             ...                        
             **                                         @=                                        
           . %*         {Fore.LIGHTWHITE_EX}Me alegra verte de nuevo{Fore.RED}        @@-          .       .                    .
          .  %=                                         @         .          .                  . 
       ..    %+                                         @=                     .              .   
      .      -@                                        -@      .                 .          .     
  ...        .@@                                     @@@@ ....                     .    .-.       
 ....           .@                                   @:    .....                         :-:-       
...               @=                                @.    . .                          -...         
..                .@@@@@@@%+=-......@@@@@@@@@@@@@@@@@   ....                         --:-.          
    .                      -:.@.....@:                  ..     .  @.                  ..    .       
      .                 .     .@....**                           .=@               :          .     
        .              .       .%@...@             ..  ..         .@@=.          .              .   
          .         .             @%.#+.         =@@%....@@+      :@::%@@      .                  : 
           ..      .               .@@@. .     :%:..........%@.   %%:@:@*..@@*.                    .
                                      @@.     @@..............@%   .@@@@::@-@ .                     
              -..                       .  ..+@................+@   .@%*@==-@@.                     
             .                            . .@*.................@=   *@*@.  .                       
           .       .                        -@...................@    @@=@   ..                    .
         .           :          %@@@@@.     *%..#.@..............@  .  @=%+     .                   
       ..             ..        @@..@@:   .@.@................:.@@:     @-@      .              .   
                         .    .@*...#@@.     @@@@+.   :*@@.....#-@-     .@-+@.@-   .                
  -:.                     .    ..:@.@@                  .#@..--..@:     %#.@@@.@.    .    ...       
:-:-.                        ....:@.=@      *@@@@@@@.@@#..@-.-...@.     .@.#@=.@.       .....       
...                         ....  @..@     .@*=::........:-:.....@    . @..@@=@=       ....         
-                         ....    :@.=@.    %@..........-:......*@.   .@:.@.@*=@.   .....           
    .                      ..     .:@.+@    .@-......:--+#%@@#++@@   *@.+@. .@-+@.    ..            
      ..                :          ..@@.@@.  @@#+:%#%@++@*=:....@+ .@#.@*    .@-#@.           ..    
        .             .                %@+=@@@....*@.+..@.......:@@:.@@.      -@-@:             .   
          .         .                  . .@@=.....@@..@@@+........#@%.         +@-@.              . 
            .     .                      .  @-.......%@*=-:......@.    .     .  #@-@.               
                                            %+.......%:+%........@               %@-@               
              ..                           .+@........@:%.......:@       ...      @@-@.             
             .                              .@..........-.......*@.     .   .      @@#*             
                                                     {Fore.RESET}jefe                """)



serpiente_menu=Fore.RESET + """
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@=@@@@@@@@@@@@@:@::@:-@@@@:#@:+@:@@@:@*@@@@@@@@@@-@@@=@@@%%%@@@#@@@%@@@@@@@@@@@@
@@@@@@@@@@@@@@#@@*+#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%@#@=@@@@@@@@@@@:@@::*+:-#@@::@::@:@@:::@@@@@:*=@@@@@-@@@=@@##%*%=+@@%+@@@@@@@@@@@@
@@@@@@@@@@@@@*%%@***@@*@#@@@@@@@@@@*@@@@@@@@@@@@@@@##*+-#@@@@@@@@@@*:::@::-@@=::::::@:::@@@:::-@@@@@@@@--@@-=@*++===+@@@@@@@@@@@@@@@@
@@@@@@+@@@@@@@@@@@@@@@+@%@@@@@@@@@@@@@@@%@@@@@@@@@@@@=--::#@-@@@@@@::+::::@@:::::@:::::@:::-:@@@@:@@@@@-:--@-@@*==+=@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@%*@@@@@@=@@@-@@@@*@@@@@--@@-::::::*@@@::@:@:::-:::-::::::::::::%@@=:@:@@@:@@::-:-@+:-@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@#*@----@@@@@@@@@@-@@@@@@@%@@@+@@@@:@@@@@@@:::::::::@::-@::::@::%::::@@::::::::=@+::::%:@:@:@@:::::@*-@@@@@@@@@@@@@@@@@@@@@
@@@+@@@@@*==+=@:-:+--@*@@@@@@-+@@@@@@@@:=@+@@=@@@@*@:::::::::::-::::::::::=@::::::::::@:::::::::::-:@::@:::::+@@@@*@@@@@@@@@@@@@@@@@@
@@@=@@@@@@@@++=---=:::@@@@:=@@@:@@@@@@@@@:::@@@@@@@@@::::::::::::::::::::%::::::::::::::::::::::::::@::::::::@@@@@@@@@@@@@@@@@=@*@@@@
@@@@@@@@=--:-:%@@@=+::@@@::=@*::@@@@@@@@@::::::@@@@@%::::::::::::::::::::::::@:::@#@::::::::::::::::@:::::::@@@@@@@@@@@@@@-@@@+@-%@@@
@@=@@@@@@@@@=::::-::::@@=@@-:+*%@@@@@@*@@@:::*:::@@@@#:::::::::::::::::::@:::::::::::::::-@::::::@=:@::::::@@@*@@@@@@@@@@@@@@#-@-+@@@
-@-@@@@@=:-%=::::=@@@@@%:::=:@@:::@@@@@@@@-:::::+::-@::::::::@::::::::::::::::::::::::::::::::::::::-:::::@@@@@@@@@@@@@@@::@@@::+:@@@
@@@@@@@@-::::::@@@@:+@@::@*:@::::::@@@@%@@%:#::::::::::::::::::::::::::::::::::::::::::::::::::*:::::@%-:@@@@@@@@@@@@@#:-@:@@=:-*-@@@
@@@@@@@@::::@@@::@@:@@@@@@::::#::#::@@@:@@@@::::::::::::::::::::::::::::::::::::--:::::@%::::-:::::::@:::@@@@@-@@@@:::=::::@@@::@*:@@
@@@@@@#*@@@@::::=@@@@@@::::#::+::::::++::@@%:::::::::::::::::::::::::::::::::::::::::::::::::::::::::@::@@@@@@:@:::::::*:::@@@::=@@@@
@@@@@@@@@-::::=::-#@@@@:@+:::::::::::::::@@@::::::::::::::::::::+@:::::::::::::::::::::::::::::::::::-::@@#@#:::::::@::@:::#@@@@@@@@@
@@@@@@@@@@:::#@@@@@@@@@@@:::::::@::::::::@@@@:::::::::::::::::::::::::::::::::::::::::::::::::::::::::@:-+:::::@@#:::::+::@@@@@@@@@-@
@@@@@@@@@@%@@@:::@@@+@@@@@@#:::::::::::::::@@::::::::::::::::::::::::::::::::::::::@::::::*-::::::::::@:::@:::@:::::::%=@@@@@@@:@@:@@
@@@@@@@@@@@+=@-##@@@*@::::@@@:::::::::::::::+:::::::::::::::::::::::::::::::::::::::::::::::::::::::::*::::::::::::::*@::@@:@@:*::=-@
@@@@@@@@@@%%%%##@@@#*+**::::::::::::::::::::::::::::::::::::+-:@@%@:-=-::::::::::::::::::::::@@::::::::@::::::::::::%::-@-:-@:::::::-
@@@@@@@@@@@@*@@@@@@#@*=#%=::-:=::::::@::::::::::::::::::=@@@@@@@@@@@@@@@+*@-@@:=:::::::::::::::::::::::@:::::::::::=#%:#:::=@::@:#:::
@@@@@@@@@@@@#@@@@@@%#%-%%%@----+-::::::::::::::::::::-@@@@@@@@@@@@@@@@@@@@@@@@@@@-::::::::::::::::::::::@::::::::::::::@::=:@:-@::@=:                           
@@@@@@@@@@@#@@@@@@@@@#%%@%@%:---=::::::::::::::::::*@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%:::::::::::::::::::@:::::-:--:::::@----@::-:-:@@
@@@@@@@@@@@@@@@@@@@@%%%@@@@@%-+=--::::::::::::::::#@@@@@@@@@@::::::::::@@@@@@@@@@@:@@@@-:::::::::::::::::*::---=%----=-@--=-@-@-=@@@@
@@@@@@@@@@@@@@@@@@#@@@%@-@@%%%#*=+*-:::::::::::::-@@@@@@@@@:::::::::::::::@%@@@@@@@@@@@@@:::::::::::::::::-----=-@==---+---:@::=@@@@@
@@@@@@@@@@@@@@@@@@%@@%%%%:%#@@##*+**:::::::::::::@@@@@@@@::::::::::::::::::::::::@@@@@@@=:::::::::::::::::==---=====-+-:::+-@@@@@@@@@
@@@@@@@@@@@@@@@@%@%%@%%@%@#@@%#%###+#::::@:::::::@@@@@@@#:::::::::::::::::::::::::::::::::@@::::-:::-----=-%-===-----:::==:@@@@@@@@@@
@@@@@@%@@@@@@@#@%@@%%@%@@%%%%@*@@##-##:::::::::::@@@@@@@@::::::::::::::::::::::::::::::::::::::::::-=-:---==@--=---:::@*-%@@@*:-:@@@@
@@@@@@@@@@@%#%@%%%@%%###%%##@@%@@=@=##:::::::::::@@@@@@@@-:::::::::::::::::::::::::::::::::::::::=+--=:-:===-=-::-:@@@@@@@@@@@@@@@*=@
@@@@@@@@@@#@%##%#%#####%#####%%#%%@@-%#:::::::::::@@@@@@@@@-:::::::::::::::::::::::::::::::::::-++===-=:+++::-::::@@@@@@@@@@@@@@@@@@@
@@@@%@@%###*#**********#***%+%#%@%%%@%%@::::::::::*@@@@@@@@@@+#=::::::::::::::::::::::::::::::====-++:=+=-::::::::@@@@@@@@=@@@%@@@@@@
@@@@@@***@@@@@@@@@@@@:*+*#:##*#:#%%+@%@@@=::::::::::@@@@@@@@@@@@@@@##-:::::::::::::::::::::::-:=++-+-+=:-==-::::@@+@@@@@:@@@@#@@@@@@@
@@+#*@@@@@@@@@@@@@@@@@@@*+*+***#:**%-#%%%-@::::::::::-@@@@@@@@@@@@@@@@@@@-::::::::::::::::::-==+:==+=:=:--:::::@@@@%@@@@@@@@@+@@@%@@@
@@@@@@@@@@@@+#@@@@@@@@@@@+++=+=+*+*=**#*@@:@@:::::::::::*@@@@@@@@@@@@@@@@@@=:::::::::::::::-=+===:-::-::::@@@@@@@-@@@:@@@@@@@@@%@@@@@
@@@@@@@@@***+=#%##@@@@@@@@+=====+*-+++#:#-%:@@:::::::::::::::-@@@@@@@@@@@@@@@::::::::::::--=-===-:::::::@@@@@@@@@@@:@@@@@@@@@*@@@@@@@
@@@@@@@=+@*@@@%@@@@@@@@@@@@@=--======+==:*-%%%@-:::::::::::::::::::@@@@@@@@@@@:::::::::::--+==::-:::@:@@@@@@%@@@@:@@@@@@@@-@@@-@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@#%@@@@@@-=-===--=-==++%#%%:::::::::::::::::::@@@@@@@@@%::::::-:=----:-::#@@@@@@@@@@@@@@:@@@@#@+@:*@+@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@*@@@@@@@---=-=-==::-+**#%%%:::--:::::::::::+@@@@@@@@@:::-----=-::::::@@@@@@@@@@@@*##*%%%@@-#:#::*@@@@@@@@@@
@@@@@@@@@@@#=@#@=@-@@%@@@@@@-@@@@@@+=----------:==**#%=::::::::::::::=@@@@@@@@@::----:::::::--:@@@@@@@@@@#-#+##@*@%*:+-:%@@@@@@@@@@@@
@@@@@@@@@@@@+@@---=+-=+*#%%%@%%@%%@@=#::-----::-=:==-+*+#=:::::::::#*@@@@@@@@@::::::-:::---:::@@@@@@@@*#%+*=#=*:*=:-:@@@@@@@@@@@+@@@@
@@@@@@@@@@@@@@@@@#=*-+=-+=++***+**###=+::-::::::---:--===+==::::*#@=@@@@@@@@@-:::::::-:--:::@@@@#%%#*%+==+=-:-::@@@@@@@@@@@@@@@@%@@@@
@@@@@@@@@@@@@@@%=:--:--=::#@@@@@@@@@@%##::::::::::::-:::----==%@@@@@@@@@@@@@:----:::--:-:+#+=#*-:=*:=-+-=:::@@@@@@@@@@@@@@@@@@@@@@#@@
@@@@@@@@@@@@@@@@@-@*:*-:@@@#-==+****@@@#*%:::::::::::::=*@@*@@@@@@@@@@@@@@@-::::::::::-*+-:=::-:=-=--:::::@@@@@@@@@@*=@@%@+@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@*#-=@@--::::::-+++@@@##+@@@%%%:::#@@@@@@@@@@@@@@@@@@@*::::::::::::=-:---::-:---:::::-@@@@@@@@@:-@@@@@@@@#@@@@@%@@@
@@@@@@@@*====@=@@-:@=@@@=@@@@@@=+=::--@@@+####**%#**@@@@@@@@@@@@@@@@@-::::::+=@@+%@@##-#:-:::::::::::::@@%*%#%@#:@*++=+=-=+=@-%#@@@@*
@@@@@@@@@@@@%+-=%+@@@:-::-+:##@@*----:@@@++=+++*@@@@@@@@@@@@@@@@@+::::::@=@@@@@@@@@@@@@@@@+@:::::::%@@#-++=@@-=-#==+-+@-:-@-+#@*@@@@@
@@@@@@@@@@@@@@@@@@@:@@@:@@:::--=@@:::-@@*::-=-@@@@@@@@@@@@@@@@::+*+=#*+@@@@@@@@@@@@@@@@@@@@*@@:=**@%##::::::#+-:--@@@@@@@@=--=@*@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@:---=+::@@@:::::@@@@@@@@@@@@@@::::-::=@#@@@@@@@@@@@@@@@@@@@@@@@@@@@=++*=::=:::::==@@@@@@@@@@@@@@+*+*@@@@
#@@@@@@@@@@@@@@@@@@@@@@*@@@@@@:::-::@@@:::::@@@@@@@@@@@@@:::::::@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@-----+=:::*@@@@-:::@%@@@@@@@@%@@#@@@"""

selva_menu=Fore.RESET + """                                                                                                                             
@@@@@@@@@@@@@@@@@@@%@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%@%:+%@@@@%%%#*%#%%*%#@*@@@@%%@@%@%%%@%@@@%%@@@@%%@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@%@@@@@@@@@@@%%@@@@@@@@@@@@@@@@@@@@@@#%@@@%%%*=#%%#%%%%%%%@*@@@@@@@%*-%@@@@%@@@@@@@%#@@@%@@%%%%%@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@%%@@@@%@%@%%%@@@@@@@%%@%@@@@@@%%@#@@@@.*@#%%--:%#%%%#%@@@%%%%%%@@%@%@@@@@@@@@@@%@@@%@@@@%@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@%#%%%%%%%%%@%@%@@%@%%%@@@@@@%%%@@@:..*-%%#%%%@%%%%%%%%%%%%*%%%%%%@#%%%%%@@@@%%%%%@%@@@@@@@@@@@@@@%@@@@@@
@@@@@@@@@@@@%@@@@@@@@@@@%%%%%%%%%###%%%@@@%%%%%%%%%@%%%%@@@:..++%%%%%%@%%%%%%%%%%%%%%@%%%%%%+*%%%@@@@#%%%@@@@@@%%@@@%@@@@@@%@@@@@
@@@@@@@@@@@@@%@@@@%%%@%%@%%%%%%%###+*%@@%%###%%%%%%%%%%%@@@%%#%%%%%%%%%%%%%%+#%%%%%%%%%%%%%+:#%%%@@@@*%%%%@%@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@%@@@@@@%%%#%%%%%%%%#**#--:#@@%@@%%#***#%%#%%%%@@@@@@#.%%%%%#%#%%%%%%%%%%%%%%%%%%%%%##%%@@@@@%#%@%@@@@@@@@@*@@@@@@@@@@@@
@@@@@@@@@@@@@@@@%%%%+%%#%%%%*%##**#:..@%@@=::-=:-.##+##@@@@@@@%%%+#*###*-#%%%%%%%%%%%%%%%%%%%%%%*%@@@@@%%@@@@%%#@@#+%%%++@@@@@@@@
@@@@@@@@@@@@@@@@@%%%%#%%%#%%%:**-.==%:@@@@.#%*#%=*++%%%@@@%%#*#*.=++#*.-*+##%%%%%%%%%%%%%%%%%%%%%%@@@@@%@%%@@@@@@@@%##%@@@%@@@@@@
@@@@@@@@@@@@@@@@%@%%%*#%#%%#%#*=.=.-%#-@@@%.%%+=##:#.#@@@@@+===+=*-=-*=-.+*#*#+##%%%%%%%+%#%%#%%%%@@@@#%@@%%@@@%@%%%=%@%@%@@@@@@@
@@@@@@@@@@@@@%@@@%%%%%%#%%%*#%##.=#.*%@@@%..#.#@@@@@@@@@@@#+***+**+*.=++++-+-+####%%%%%%%%#+###%%%@@@@%*%%%@%%%%+%*%%+=%@#@@@@@@@ 
@@@@@@@@@@@@@@@@@@%%%%%%@%+*%::=%#@%%%@@@%@@@@@@@@@@@@@@@##%##=+*****+=::.:...**#########%#.###%%%@@@@%%%%%%%%%%@*%%*+*+###@%@@@@
@@@@@@@@@@@@%%%@%%%%#%%#%%%#**.#==%%%%%@@@@@@@@@@@@#+*.*########***+*+......:+**#########*+**##.**%@@@@@#%%%@%%@%%#=+***###@%@@@@
@@@@@@@@@@@@@@@%@#%#%%%*#%%%%%.%*#%:%@@@@@@@%=%*#@%###*+.+*###*+****+=......-.++*****##*#****#+-#**@@@@@%%@@@%@@@%##*#####%@%@%@@
@@@@@@@@@@@@%%%%#%%%%#+%%-*##%#%%+=%@@@@@@@##:#+*+#**==**#*###+.=+*++.......-==+++++***#+=.-=+*+*+*%@@@@@@@@@%%@%@@@@@@@%%%@%@%@@
@@@@@@@@@@@@@%%@%%#%#%%###=:...=+%%@@@@@%##**%:..===.+=++.*****=--+++-......:--:===+++++=.::==-=***#@@@@%%@@@@@%@@@@@%%%%%%@%%@@@
@@@@@@@@@@@@@@%%%%%%#%%%%##*..=%%%+@@@@@#%%+-#-...==+++.:=-:=:+*++++=-:-.....:..:--:.-=+++=.-.-+=++#%@@@%@%%@%@%@%@@%%%%%%%@%%@@@
@@@%@@@@@@@@@@@@%%@@@%%###+####%%%%@@@@@%#=%%##.......-..:=:--+*+++.---:.........::..--:..=-=-:-==+*#@@@@*##%%%%%%%%%@@@%@%@%@@@@                                       
@@@@%@%@@@@@@%@@@@@@@@%%**++-=.=%**@@@@@%=.%%-........#******++=-:..::.:........:...........:..-..*=@@@@@@%@@@%%@@@%%@@@@%%@@@@@@
@@@@@%%%@@@@@@%%@@@###@@@@@+++==%*#@@@@%*%%%-.....:###*****=-........:.........................%%*%#@@@@+*@@@@@@@@%@%@@@@@%%@%@@@                                       
@@@@%@%%%@@@@@%####*##***@@%%%**#+%@@@@%%%%#.....#*###*.*=..................................:..%+@*@@@@@@%@%%@@@@%@@%@@@@%%%@@@@@       
@@@@%%%%%@@@@@%%##*##*#*+++%@@@@#@@@@@@%%.%.....#####*..*................................#.%%%#@@%@@@@@@+*#@%%%@%%%%%%%%@@@%@@@@@                                       
@@@@@@@@%@@@@@@@%#####+==++=+%@@@@@@@*%%%.@.....####*...-...............................#%#%@@%@%@+@@@@%##%###%%#%%%%%%%@%%%@@@@@
@@@@@@@@@@@@@@@%#***+****+:++@+%@@@%===%%%%..:.####*..:................................+%%#%%#%@%@%@@@@@*%%**#%####%%%%%@%%%@@@@@                                      
@@@%@@@@@@@@@@@#****+##-=*+**@=%@@%--::%%%%..+####*...................................%%%%%@#%-.%#:@@@%*+=++***#####%%%%@%%%%@@@@
@%%@@@@%@@@@@@@@***++**+=++--#@@@@*.-=:%%%%%%%###*..................................:=:-#=%+%#...**@@@@#@-++++**######%%%%%%%@@@@                                       
@@@@%@%@@%@@@@@@@**++*==*=--:-@@@@%@@@@@%%%%%%#*+...................................#=...%%:...=@.%-@@@@:*@=++***######%%@%%@@@@@
@@@%%%%%%##@@@@@@#+++*==-=:::.@@@@@@@@@@@%%%#........................................*..#....#+%@=.@@@@@::@==++**%@#*##%@@%@@@@@@                            
@@@@%@%%%#@%@@@@@@++-+-==-...@@@@@@@@%%%%..%:..........................................-#....:.....@@@@...+@==++@@@#%%#@@@@@@@@@@
@@@@@%@@%%%*+@@@@@*==#:-....@@@@@@@%.#.%%.-%.............................@@@@%.....................@@@@..:.:%=+++*@@@#@%@@@@@@@@@                      
@%%%%%##%*%@*+@@@@@+.*.+:..:@@@@@@-..#.%%..@.............................@@@@@@@@@@@-..............@@@@....::+=#@@@###%%@@@@@@@@@
%@@%%####***++@@@@@:.:....=.@@@@@......%%..%.............................#.@@@@@@@@@@@%............@@@@=:..::*==+@**%@@%@@@@@@@@@                              
@%%%%###***++@@@@@@:....=--%@@@@@.=....%%..#=..............................=@@@@@@@@@@@@@...........@@@%....:-%++++%@@%%@@@@@@@@@
%@%%%###*****%#@@@@-+:.-=:-@@@@@@%.....%%.#%................................@@@....=@@@@@@@.........@@@@...:::-%+++**#%@@@@@@@@@@
%%%%####**##=*%@@@@@.:=--.*-@@@@@@.-.*:%%.#%...............................@@@#..@@@@@@@@..@=........@@@@..::--=%++*@%*@@@@@@@@@@
%%%%###%@#**@@*@@@@@:.....@%@@@@@=:..-.%%.%%.............................%@..@...@@...@@@...%@.......@@@@@:::---@+*+%*@@@@@@@@@@@
%%%%%@@@%@@@@@@@@@@@-.....@@@@@@%#.....%%.:%................::...........%=..@...@@=.@@@......@......@@@@@.::=%=@###%@%@%@@@@@@@@
%%%%%@@@@@@@@@@@@@@@*=*..#@@@@@@-......:%.#%....................-.---.+**#...@..+.@@.@@@.......@.....@@@@@:::-%##%%%@@@%@%@@@@@@@
@@@@@%@%#@@@@@+@@@@@%%-:%%@@@@@@+......@%.*%................##*.:=**####%%%%%@@@@@%...%%@+......@....@@@@@::--==+@%@@@@@@@@@@@@@@
@@@@@@@%####**#@@@@@@-@=.@@@@@@@.#.....@%.@@..%............#..**##.%%%%%%%%@@@@@@@@@@@@@%@@.....=-...@@@@@@@-%#+%%@%@@@@@@@@@@@@@
@@@@%@%@%##@%#@@@@@@@#@@@@@@@@@@.-....%@..@@@@%%.:%.%.......=.....%%%%%%%@@@@@@@@@@@@@@@@@@@.@-.%...@@@@@@@@@*#%@%@%@@@@@@@@@@@@@
@@@@@@%%%@%@%%%@@@@@@#===@@@%@@@%-....+%@@%:@@%.%%%................+%@@@@@@@@@@@@@@@@@@@@@@@@@@:..=@@@@@@%@@@@@@@@%@@@@@@@@@@@@@@
@@@@@@@%@%%@@%@@@@@@@%*==@@@@@@@=:...@@%#.@#%%@@:@.:............%.%@*%@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%@%@@@@@@@@@@@@@@@@@@@@
@@@@@@@@%%%%##@@@@@@##*++@@@%@@@@@::@@%@@:@.:%%@%.............%%#.%@%%%@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@%%%%#%@@@@@@#***@@@@%@@==@@@@%@@..%.-..%+.............%%#...%#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@%@@%@%@%@@@@@@@@##*@@@@@@@@@%*%--%@%%%:+#=#............+:.:%@*@*.@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@"""

casa_menu=f"""{Fore.RESET}
*********************************************************************************************************************
*********************************************************************************************************************
*********************************************************************************************************************
*********************************************************************************************************************
***************************************************************************###%##%##*********************************
**************************##%*****************************************#%%#%%#%%%%%%%###%##***************************
*********************##**#%@%#**********************************%###%%%@@@@%@@@@@@@%@%#%%#####***********************
*********************#%@**%%@%**%###%%************************#%%%#%@@%%%@%@@@@@@@@%%%%@%@%%#%%**********************
**********************%%@%#@@#%%#%@%@#*********************##%%%@%%@@@@@%@@@%@@%@@@#%#%%%@@%%@%%%%#******************
**********************%@@@@%@%%%%@%%%#*********************##%%@@@@@%@@###%%#@%%@@@@@@@%@@@@@@%@@%#******************
**************#%@%#****#%%@@@@#%@@%#*****%%##************##%@@@%@@%@@@%%%%%%%@#%%%%%%@%%#%%#@@@@@@%%##***************
***********#%%%#%@%@%@@@%@@@@@@@@%##@@%%##*#**********#%%%@@@@@@@#%##%@@@@@@@@@@@@%%@%@@@@@@@@%@@@%@@%#**************                            
**************%*#*#%%@%%@@@%@@@@@@@%##*************####%%@%@@@@@%%%@%@@@@@@@@@@@@@@@%@@@@@@@%%#%%@@@@@%@#************
********************%@#%%%@@@@%@%%#%%#%@@@%********##@@@@#%%@@@%@@@@@@@@@@@@@@@@@%%@@@@@@@@@%@@@@%%#@@@@@#***********
*********************%@@@@@@@@@@%%%#%%%%%%%#******%#%%%%@@@@@@@@@@@@%@@@@#@%@*%%%@#%#@@%@@@@@@@@@@@%%@%@*************                             Hemos entrado en la casa y todo es un desastre, está todo desordenado,
*****************%@@@@@#%@@%%%%@%@@%##%%%#******#%%@@%@%@@@@@@%%%#@@@@@**@*@**@#@@**%@@@@@@@@@%@@@@@@%%%%************
**************%@@%%@##*%%%%%%%#@@%@@@###%#%#***#%%%%@@@%@%%%%**%*#*##%@#**%%@*%%**%@*%**@#%@@@@@@@@@@@@%%%***********                             tirado por el suelo y no hay nada de valor, hay muchas cosas,
************@@%@@#****%%%%#@@%%%@@##@@@@**********###%%*@#%**@%#@#%%*#@#**@@*#%@@#**@@@**#@%@%%%#%%#%%%@@%#**********
***********@##*#******%%@%#%#@%@#%@%*%@@@#****************%%***#**@#*%*@@@#***@*@@*@@#*#@%#@*#%@%%%%%%%**************                             pero podríamos decir que todo lo que hay es basura. 
**********%*****##%**@%@@#@%#@@*%#@%**#%#@#******%**********@****@*@##**%@*@@**##@@%@@***%%%#@*%%#%%%%%**************
****************%%%%@%%%#@@#*%%#*#@%*****#*#******************@#***@***%*@**@*#**@@@**#%*****##%%%%%%%%%%************
*******%#%%%%%@**%%%@@@%#%@#*@*****##**************@@%@#*************@#@**@@#%@*@@**#**@*#**###%%%%%%%%****%*********                             Lo único que parece mantenerse en un estado medio bueno es 
*********%@%#%#%%%%@@@%@@%%#%@%%#***#***#*********#@@@%%%@@#**********@#@**@*@@@@*@#**@**@##*##*%*#%#*%*##*%*********
*******#*######@%@@%@@@%#@%#%@******************#@@@@@@@###%#%%#*******@@**%%*@@%*%%@#*#######%####%*#*#*%%#*********                             un bote con un líquido extraño, tiene una etiqueta que pone... veneno.
****************#%%@@@#@%@@%@@@@%%*************@@@@@%@@@#@%%%##%###@#*****@@#@@@***####*##########***%*#%%#%*********
***********%@@%%%@@@@@%%%##*@*****************@%@@@@@%%@@@%###%#%##%%%%@%***@@@%@@%%#**#########%%%**#%#####*********                             Por otro lado, parece que también hay un papel que está en buen estado,
******%*%@%@##%@@@%@@@@%%#@@@@%**************%@@@%%#%#%@#%@@%%###%%###%#%#%%%#%%##%@@***########%#%%%#####%@*********
*******%@%###@@%%#%@@@%%@%%%@#%#%%*********@@@@@@%%%@#@%%%%@@#%*%#%%%%#@%%@##%%#%%@@@@*#####*%#%#%#%%%@%@#%@*********                             parece que muestra un dibujo, parece una especie de mapa.
****##%%%%%@@@###%@%%@@**%%@@####%%%******@%@@@@@#%@#@@@#%@@@@@@#@%%%%%#%@%%%%%#@@@@@@@###*####%#%%#@@%%%%%%@#*******
*****##%%%@%%%%**%%*#@@#*#%@@@%****##****%#@@@@@@@@%@@@@@%@%%@@@@@@@@%%@#%%%%%#%@@@@@@@#*####%@@%##@@@@*@@%@%********
*****%%#%%%%%%***@%*%@#@@**%@#@%*******@@@@@@@@@@@@#@@**@%%%@%%@@@@@*%@@@@@@@@@@@@@%@@@@#*###*#%@##%@%%%@@%%#%%******                             
****%**@%@%%#%###@*#@@#%%#**@#%%#************@@@@@%%#@**@#%@@@@@@@@@**@@@@@@@@@@*@%@@@@@@#*##%%@%%%##%@%%@@@@#*******
******%####%##*#****%@%*%#**@**#@@***********@@@@@@**@**#@@@@%%@@@@@*#@@@%@@@@@@*@@@@@****###@#%#@@%@%@%@@@@#********                             
******#**#**#****#**#@#**#**@***##***********@##%@%#%##@@@@@@%#%@@@@@@@@@@@@@@@@#@@@@@**#%######@%%%@@%@@%@%%%*******
*******##*#*#***###**@#**#**@**********#@%@@@@@%#%%##@@@@@@@#%%#@%%@#@%%@%@@@@@@%@@@@@**#%#%%%%%@%@%@@@%@@%@%@*******
*******#####*########@###***@**********@@%##%#%@@@@@@@@@@%#%@@@@@%#@%#@#%##@%%%@@%%@@@#%%##%%%%@@####@##@%@@#********
********###**########@###*##@*******#%@@@@@@@@@%@%@@@@%%%@@%@@%#%@%##@##%@%##@#@##@#@#@#@@%#%####%%#@@#@##@@##%******                            
*****#######%#%%%#%##@###*##@###**@%%%%%@@%%#%%#%##@%#%%%##%%@@@%##%@@@@@@@@@@@##@@#%@#@#%%%%@@###@%%@@@@@@%@%*******
****%%@%%####*##%%*##@*##*##@%@%#%%%#%%@@@%%#%%@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%@@%%@#@@%%@%#%@********
***#*%%#%@%%#%%%%##*#@#####%@##@@@@%%%##%@@@@@@@@@@@@@@*#@@@@@#@@@@@@@@@%@@@@@%@@@@@@@*#@*@*#@@%#%@%@%@#%#%@%********
*****#%%#@%%#%%%@####@##*###@##**%****#**@**@%@@@@@@@@@@@@@@@@%@@@@@@@@@@@@@@@%@@@%@@@####@#%@%%@%%%%%@#%#%@@********
****%@%#%#@%#%#%%%##%@#####%@##**#****%**@**@%@%@@@%@@@%@@@@@@%@@@%@@%@@@@@@@@%@@@@@@@#%##@%%@@@@#@@#%@@@@@@@@*#*****
****%%@%##@%%%@%#####@%#%##%@##*#%##*#%##@#%@@%%%@@%%@%%@@@@%@#%@@@@@@%@@@@@@@@@@##%@@%%#%@%%@%#@#%@%@%%#@@@@#*******
****%@#*%@@%##@%%#%#%@#%%##@@**#@%%##%%##%%%@%#%%%@%@@%%@%@%@@%%#%%%%@%#@@@@@@#%##%%@@@@@@@#@@#%#%%%#@@*%@#%@********
****#@@%##*####%@%%%#@%%%%%@@###@%%%%%%%%%%#%%%%%%@%@@%@@@@%@%%%%%@@*###%#@@@@#%@##%@@@@%##%#%#%#%#@%@#@@@%#@%%******"""

pantano=f"""
                          {Fore.GREEN}#####
                       #######
            ######    ########       #####                                     {Fore.RESET}Hemos llegado a un pantano lleno de cocodrilos, aunque entre ellos, hay{Fore.GREEN}
        ###########/#####\#####  #############                                 {Fore.RESET}un cocodrilo inmensamente grande que nos bloquea el camino. Seguramente {Fore.GREEN} 
    ############/##########--#####################                             {Fore.RESET}sea el monstruo del que hablaba el jefe de la tribu, porque su tamaño es{Fore.GREEN}          
  ####         ######################          #####                           {Fore.RESET}sobrenatural.{Fore.GREEN}  
 ##          ####      ##########/@@              ###                          {Fore.RESET}Abre el menú para ver que podemos hacer, recuerda que tienes el mapa por{Fore.GREEN}
#          ####        ,-.##/`.#\#####               ##                        {Fore.RESET}si ninguna de las opciones es viable, quizás te falte algo de otra zona.{Fore.GREEN}
          ###         {Fore.RESET}/  |$/  |,-. {Fore.GREEN}####                 #
         ##           {Fore.RESET}\_,'$\_,'|  \  {Fore.GREEN}###
         #              {Fore.RESET}\_$$$$$`._/   {Fore.GREEN}##
                          {Fore.RESET}$$$$$_/     {Fore.GREEN}##{Fore.RESET}                                                                                                                                                            ___
                          {Fore.RESET}$$$$$        {Fore.GREEN}#{Fore.RESET}                                                                                                                                                      _,-'""   ""'"`--.
                          {Fore.RESET}$$$$$                                                                                                                                                            ,-'          __,,-- \\
                          $$$$$                                                                                                                                                          ,'    __,--"'""dF      )
                          $$$$$                                                                                                                                                         /   .-"Hb_,--""dF      /
                          $$$$$                                                                                                                                                       ,'       _Hb ___dF"-._,-'
                         $$$$$                                                                                                                                                      ,'      _,-""'"   ""--..__
                         $$$$$                                                           {Fore.LIGHTGREEN_EX}_.---._     .---.{Fore.RESET}                                                                         (     ,-'                  `.
                         $$$$$                                                   {Fore.LIGHTGREEN_EX}__...---' .---. `---'-.   `.  {Fore.RESET}                                                                     `._,'     _   _             ;
                         $$$$$                                         {Fore.LIGHTGREEN_EX}~ -~ -.-''__.--' _.'{Fore.YELLOW}( | ){Fore.LIGHTGREEN_EX}`.  `.  `._ :  {Fore.RESET}                                                                      ,'     ,' `-'Hb-.___..._,-'
                         $$$$$                                        {Fore.LIGHTGREEN_EX}-.~~ .'__-'_ .--'' ._`---'_.-.  `.   `-`.   {Fore.RESET}                                                                   \    ,'"Hb.-'HH`-.dHF"
                        $$$$$                                          {Fore.LIGHTGREEN_EX}~ ~_~-~-~_ ~ -._ -._``---. -.    `-._   `.     {Fore.RESET}                                                                `--'   "Hb  HH  dF"    
                        $$$$$                                            {Fore.LIGHTGREEN_EX}~- ~ ~ -_ -~ ~ -.._ _ _ _ ..-_ `.  `-._``--.._     {Fore.RESET}                                                                  "Hb HH dF
                        $$$$$                                             {Fore.LIGHTGREEN_EX}~~-~ ~-_ _~ ~-~ ~ -~ _~~_-~ -._  `-.  -. `-._``--.._.--''. ~ -~_  {Fore.RESET}                                                   "HbHHdF
                        $$$$$                                                 {Fore.LIGHTGREEN_EX}~~ -~_-~ _~- _~~ _~-_~ ~-_~~ ~-.___    -._  `-.__   `. `. ~ -_~    {Fore.RESET}                                               |HHH|
                       $$$$$                                                      {Fore.LIGHTGREEN_EX}~~ _~- ~~- -_~  ~- ~ - _~~- _~~ ~---...__ _    ._ .` `. ~-_~    {Fore.RESET}                                              |HHH|
                       $$$$$                                                         {Fore.LIGHTGREEN_EX}~ ~- _~~- _-_~ ~-_ ~-~ ~_-~ _~- ~_~-_~  ~--.....--~ -~_ ~     {Fore.RESET}                                             |HHH|
                       $$$$$                                                             {Fore.LIGHTGREEN_EX} ~ ~ - ~  ~ ~~ - ~~-  ~~- ~-  ~ -~ ~ ~ -~~-  ~- ~-~     {Fore.RESET}                                               |HHH|
                       $$$$$                                                                                                                                                                    |HHH|
                       $$$$$                                                                                                                                                                    |HHH|
{Fore.BLUE}~~~~~~~~~~~~~~~~~~~~~~~{Fore.WHITE}$$$$${Fore.BLUE}~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~{Fore.WHITE}|HHH|{Fore.BLUE}~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~{Fore.RESET}
                       $$$$$                                                                                                                                                                    |HHH|
                       $$$$$                                                                                                                                                                    |HHH|        
                       $$$$$                                                                                                                                                                    |HHH|            
                      $$$$$$$                                                                                                                                                                   dHHHb                
                      $$$$$$$                                                                                                                                                                 .dFd|bHb.                    
                     $$$$$$$$$                                                                                                                                                              .dHFdH|HbTHb.
_____________________$$$$$$$$$_____________________________________________________________________________________________________________________________________________________________dHHFdHH|HHhoHHb______________________________

"""


pantano2=f"""
                          {Fore.GREEN}#####
                       #######
            ######    ########       #####                                     {Fore.RESET}El cocodrilo está derrotado, y el camino se ha quedado libre.{Fore.GREEN}
        ###########/#####\#####  #############                                 {Fore.RESET}Es curioso, su cuerpo se ha sumergido en el pantano y ha desaparecido, {Fore.GREEN}
    ############/##########--#####################                             {Fore.RESET}solo ha quedado de él un colmillo gigante en la orilla. {Fore.GREEN}        
  ####         ######################          #####                             
 ##          ####      ##########/@@              ###                          
#          ####        ,-.##/`.#\#####               ##                        
          ###         {Fore.RESET}/  |$/  |,-. {Fore.GREEN}####                 #
         ##           {Fore.RESET}\_,'$\_,'|  \  {Fore.GREEN}###
         #              {Fore.RESET}\_$$$$$`._/   {Fore.GREEN}##
                          {Fore.RESET}$$$$$_/     {Fore.GREEN}##{Fore.RESET}                                                                                                                                                            ___
                          {Fore.RESET}$$$$$        {Fore.GREEN}#{Fore.RESET}                                                                                                                                                      _,-'""   ""'"`--.
                          {Fore.RESET}$$$$$                                                                                                                                                            ,-'          __,,-- \\
                          $$$$$                                                                                                                                                          ,'    __,--"'""dF      )
                          $$$$$                                                                                                                                                         /   .-"Hb_,--""dF      /
                          $$$$$                                                                                                                                                       ,'       _Hb ___dF"-._,-'
                         $$$$$                                                                                                                                                      ,'      _,-""'"   ""--..__
                         $$$$$                           {Fore.BLUE}~                                                                           ~{Fore.RESET}                                             (     ,-'                  `.
                         $$$$$                                                                                                                                                      `._,'     _   _             ;
                         $$$$$                                                                                                                                                       ,'     ,' `-'Hb-.___..._,-'
                         $$$$$                                                                                                                                                       \    ,'"Hb.-'HH`-.dHF"
                        $$$$$                                                                                                                                                         `--'   "Hb  HH  dF"    
                        $$$$$                                                                                                                                                                 "Hb HH dF
                        $$$$$                                               {Fore.BLUE}~                                ~                                             ~{Fore.RESET}                                   "HbHHdF
                        $$$$$                                                                                                                                                                   |HHH|
                       $$$$$                                                                                                                                                                    |HHH|
                       $$$$$                                                                                                                                                                    |HHH|
                       $$$$$                                                                                                                                                                    |HHH|
                       $$$$$                                                                                                                                                                    |HHH|
                       $$$$$                                                                                                                                                                    |HHH|
{Fore.BLUE}~~~~~~~~~~~~~~~~~~~~~~~{Fore.WHITE}$$$$${Fore.BLUE}~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~{Fore.WHITE}|HHH|{Fore.BLUE}~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~{Fore.RESET}
                       $$$$$                                                                                                                                                                    |HHH|
                       $$$$$                                                                                                                                                                    |HHH|        
                       $$$$$                                                                               ,-.__..-;                                                                            |HHH|            
                      $$$$$$$                                                                              `._..-´                                                                              dHHHb                
                      $$$$$$$                                                                                                                                                                 .dFd|bHb.                    
                     $$$$$$$$$                                                                                                                                                              .dHFdH|HbTHb.
_____________________$$$$$$$$$_____________________________________________________________________________________________________________________________________________________________dHHFdHH|HHhoHHb______________________________

"""


pantano3=f"""
                          {Fore.GREEN}#####
                       #######
            ######    ########       #####                                     
        ###########/#####\#####  #############                               
    ############/##########--#####################                                      
  ####         ######################          #####                             
 ##          ####      ##########/@@              ###                          
#          ####        ,-.##/`.#\#####               ##                        
          ###         {Fore.RESET}/  |$/  |,-. {Fore.GREEN}####                 #
         ##           {Fore.RESET}\_,'$\_,'|  \  {Fore.GREEN}###
         #              {Fore.RESET}\_$$$$$`._/   {Fore.GREEN}##
                          {Fore.RESET}$$$$$_/     {Fore.GREEN}##{Fore.RESET}                                                                                                                                                            ___
                          {Fore.RESET}$$$$$        {Fore.GREEN}#{Fore.RESET}                                                                                                                                                      _,-'""   ""'"`--.
                          {Fore.RESET}$$$$$                                                                                                                                                            ,-'          __,,-- \\
                          $$$$$                                                                                                                                                          ,'    __,--"'""dF      )
                          $$$$$                                                                                                                                                         /   .-"Hb_,--""dF      /
                          $$$$$                                                                                                                                                       ,'       _Hb ___dF"-._,-'
                         $$$$$                                                                                                                                                      ,'      _,-""'"   ""--..__
                         $$$$$                           {Fore.BLUE}~                                                                           ~{Fore.RESET}                                             (     ,-'                  `.
                         $$$$$                                                                                                                                                      `._,'     _   _             ;
                         $$$$$                                                                                                                                                       ,'     ,' `-'Hb-.___..._,-'
                         $$$$$                                                                                                                                                       \    ,'"Hb.-'HH`-.dHF"
                        $$$$$                                                                                                                                                         `--'   "Hb  HH  dF"    
                        $$$$$                                                                                                                                                                 "Hb HH dF
                        $$$$$                                               {Fore.BLUE}~                                ~                                             ~{Fore.RESET}                                   "HbHHdF
                        $$$$$                                                                                                                                                                   |HHH|
                       $$$$$                                                                                                                                                                    |HHH|
                       $$$$$                                                                                                                                                                    |HHH|
                       $$$$$                                                                                                                                                                    |HHH|
                       $$$$$                                                                                                                                                                    |HHH|
                       $$$$$                                                                                                                                                                    |HHH|
{Fore.BLUE}~~~~~~~~~~~~~~~~~~~~~~~{Fore.WHITE}$$$$${Fore.BLUE}~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~{Fore.WHITE}|HHH|{Fore.BLUE}~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~{Fore.RESET}
                       $$$$$                                                                                                                                                                    |HHH|
                       $$$$$                                                                                                                                                                    |HHH|        
                       $$$$$                                                                                                                                                                    |HHH|            
                      $$$$$$$                                                                                                                                                                   dHHHb                
                      $$$$$$$                                                                                                                                                                 .dFd|bHb.                    
                     $$$$$$$$$                                                                                                                                                              .dHFdH|HbTHb.
_____________________$$$$$$$$$_____________________________________________________________________________________________________________________________________________________________dHHFdHH|HHhoHHb______________________________

"""

cofre=(Fore.LIGHTWHITE_EX + """



                                                                                                




                                                   )                                                                                                                  )     
          (                                       /(                                                                                                                 /( 
          )\                                     (  \                                                                                                               (  \      
         /  )                                    ) * )                                                                                                              ) * )     
        ( * (                                     \#/                                                                                                                \#/                                 (
         \#/                                    .-"#'-.                                                                                                            .-"#'-.                               )\\
       .-"#'-.                               (  |"-.='|                                          Este cofre parece que está cerrado.                            (  |"-.='|                              /  )
       |"-.-"|                               )\ |     |                                                                                                         )\ |     |                             ( * (
       |     |                              /  )|     |                                                                                                        /  )|     |                              \#/
       |     |                             (   (|     |                                                                                                       (   (|     |                            .-"#'-.
       |     |                              ) . )     |                                                                                                        ) . )     |                            |"-.-"|
       '-._,-'                               \#/|     |                                               ____...------------...____                                \#/|     |                            |     |
                                           .-"#'-.    |                                          _.-"` /o/__ ____ __ __  __ \o\_`"-._                         .-"#'-.    |                            |     |
                                           |"=,-"|    |                                        .'     / /                    \ \     '.                       |"=,-"|    |                            |     |
                                           |  !  |    |                                        |=====/o/======================\o\=====|                       |  !  |    |                            |     |
                                           |     |    |                                        |____/_/________..____..________\_\____|                       |     |____|                            |     |
                                           |     |____|                                        /   _/ \_     <_o#\__/#o_>     _/ \_   \                       |     |                                 '-._,-'
                                           |     |                                             \   \   /________\####/________\   /   /                       |     |
                                           '-._,-'                                              |===\!/========================\!/===|                        '-._,-'
                                                                                                |   |=|          .---.         |=|   |
                                                                                                |===|o|=========/     \========|o|===|
                                                                                                |   | |         \() ()/        | |   |
                                                                                                |===|o|======{'-.) A (.-'}=====|o|===|
                                                                                                | __/ \__     '-.\\uuu/.-'    __/ \__ |
                                                                                                |  \   /  ==== .'.'^'.'.====  \   /  |
________________________________________________________________________________________________|  _\o/   __  {.' __  '.} _  _ \o/ _ |_____________________________________________________________________________________________________
                                                                                                -------------------------------------- 

             
       
       
       
       """)




cofre_open=(Fore.LIGHTWHITE_EX + """
            
______________________________________________________________________________________________________________________________________________________________________________________________________________________________________
                    |                   |                   |                   |                   |                 |                   |                   |                   |                   |                   |
____________________|___________________|___________________|___________________|___________________|_________________|___________________|___________________|___________________|___________________|___________________|____________
            |                   |                   |                   |            |                   |                   |                   |                   |                   |                   |                   |
____________|___________________|___________________|___________________|____________|___________________|___________________|___________________|___________________|___________________|___________________|___________________|___
                    |                   |                   |                   |                                                         |                   |                   |                   |                   |
____________________|___________________|___________________|___________________|_____       _______ _                           _        |___________________|___________________|___________________|___________________|____________
            |                   |                   |                   |            |      |__   __| |                         | |              |                   |                   |                   |                   |
____________|___________________|___________________|___________________|____________|         | |  | |__   ___    ___ _ __   __| |       _______|___________________|___________________|___________________|___________________|___
                    |                   |                   |                   |              | |  | '_ \ / _ \  / _ \ '_ \ / _` |       |                   |                   |                   |                   |
____________________|___________________|___________________|___________________|_____         | |  | | | |  __/ |  __/ | | | (_| |       |___________________|___________________|___________________|___________________|____________
            |                   |                   |                   |            |         |_|  |_| |_|\___|  \___|_| |_|\__,_|              |                   |                   |                   |                   |
____________|___________________|___________________|___________________|____________|                                                    _______|___________________|___________________|___________________|___________________|___
                    |                   |                   |                   |                                                         |                   |                   |                   |                   |
____________________|___________________|___________________|___________________|_____                 ¡Gracias por jugar!                |___________________|___________________|___________________|___________________|____________
            |                   |                   |                   |            |                                                           |                   |                   |                   |                   |
____________|___________________|___________________|___________________|____________|___________________________________________________________|___________________|___________________|___________________|___________________|___
                    |                   |                   |                   |                   |                 |                   |                   |                   |                   |                   |
____________________|___________________|___________________|___________________|___________________|_________________|___________________|___________________|___________________|___________________|___________________|____________
            |                   |                   |                   |            |                   |                   |                   |                   |                   |                   |                   |
____________|___________________|___________________|___________________|____________|___________________|___________________|___________________|___________________|___________________|___________________|___________________|___
                    |                   |                   |                   |                   |                 |                   |                   |                   |                   |                   |
____________________|___________________|___________________|___________________|___________________|_________________|___________________|___________________|___________________|___________________|___________________|____________
            |                   |                   |                   |                   |                   |                   |                   |                   |                   |                   |
____________|___________________|___________________|___________________|___________________|.=""_;=.___________|___________________|___________________|___________________|___________________|___________________|__________________
|                   |                   |                   |                   |        ,-"_,=""     `"=.            |                   |                   |                   |                   |                   |
|___________________|___________________|___________________|___________________|________"=._o`"-._        `"=._______|___________________|___________________|___________________|___________________|___________________|____________
          |                   |                   |                   |                   |  `"=._o`"=._      _`"=._           |                   |                   |                   |                   |                   |
 _________|___________________|___________________|___________________|___________________|_______:=._o "=._."_.-="'"=.________|___________________|___________________|___________________|___________________|___________________|
|                   |                   |                   |                   |          __.--" , ; `"=._o." ,'""-._ ".                 |                   |                   |                   |                   |
|___________________|___________________|___________________|___________________|_______._"  ,. .` ` `` ,  `"-._"-._   ". '_______________|___________________|___________________|___________________|___________________|____________
          |                   |                   |                   |                 |o`"=._` , "` `; .". ,  "-._"-._; ;    |                   |                   |                   |                   |                   |
 _________|___________________|___________________|___________________|_________________| ;`-.o`"=._; ." ` '`."\` . "-._ /_____|___________________|___________________|___________________|___________________|___________________|
|                   |                   |                   |                   |       |o;    `"-.o`"=._``  '` " ,__.--o;                |                   |                   |                   |                   |
|___________________|___________________|___________________|___________________|_______| ;     (#) `-.o `"=.`_.--"_o.-; ;________________|___________________|___________________|___________________|___________________|_____________
____/______/______/______/______/______/______/______/______/______/______/______/______|o;._    "      `".o|o_.--"    ;o;____/______/______/______/______/______/______/______/______/______/______/______/______/______/______/
/______/______/______/______/______/______/______/______/______/______/______/______/____"=._o--._        ; | ;        ; ;/______/______/______/______/______/______/______/______/______/______/______/______/______/______/______/
____/______/______/______/______/______/______/______/______/______/______/______/______/_____"=._o--._   ;o|o;     _._;o;____/______/______/______/______/______/______/______/______/______/______/______/______/______/______/
/______/______/______/______/______/______/______/______/______/______/______/______/______/______/"=._o._; | ;_.--"o.--"_/______/______/______/______/______/______/______/______/______/______/______/______/______/______/______/
____/______/______/______/______/______/______/______/______/______/______/______/______/______/______/_"=.o|o_.--""___/______/______/______/______/______/______/______/______/______/______/______/______/______/______/______/
/______/______/______/______/______/______/______/______/______/______/______/______/______/______/______/______/_________/______/______/______/______/______/______/______/______/______/______/______/______/______/______/______/
___/______/______/______/______/______/______/______/______/______/______/______/______/______/______/______/_________/______/______/______/______/______/______/______/______/______/______/______/______/______/______/______/_____
/______/______/______/______/______/______/______/______/______/______/______/______/______/______/______/______/_________/______/______/______/______/______/______/______/______/______/______/______/______/______/______/______/
___/______/______/______/______/______/______/______/______/______/______/______/______/______/______/______/_________/______/______/______/______/______/______/______/______/______/______/______/______/______/______/______/_____
/______/______/______/______/______/______/______/______/______/______/______/______/______/______/______/______/_________/______/______/______/______/______/______/______/______/______/______/______/______/______/______/______/
___/______/______/______/______/______/______/______/______/______/______/______/______/______/______/______/_________/______/______/______/______/______/______/______/______/______/______/______/______/______/______/______/_____
/______/______/______/______/______/______/______/______/______/______/______/______/______/______/______/______/_________/______/______/______/______/______/______/______/______/______/______/______/______/______/______/______/
___/______/______/______/______/______/______/______/______/______/______/______/______/______/______/______/_________/______/______/______/______/______/______/______/______/______/______/______/______/______/______/______/_____
/______/______/______/______/______/______/______/______/______/______/______/______/______/______/______/______/_________/______/______/______/______/______/______/______/______/______/______/______/______/______/______/______/
___/______/______/______/______/______/______/______/______/______/______/______/______/______/______/______/_________/______/______/______/______/______/______/______/______/______/______/______/______/______/______/______/     
/______/______/______/______/______/______/______/______/______/______/______/______/______/______/______/______/_________/______/______/______/______/______/______/______/______/______/______/______/______/______/______/______/
___/______/______/______/______/______/______/______/______/______/______/______/______/______/______/______/_________/______/______/______/______/______/______/______/______/______/______/______/______/______/______/______/ 
/______/______/______/______/______/______/______/______/______/______/______/______/______/______/______/______/_________/______/______/______/______/______/______/______/______/______/______/______/______/______/______/______/
___/______/______/______/______/______/______/______/______/______/______/______/______/______/______/______/_________/______/______/______/______/______/______/______/______/______/______/______/______/______/______/______/
/______/______/______/______/______/______/______/______/______/______/______/______/______/______/______/______/_________/______/______/______/______/______/______/______/______/______/______/______/______/______/______/______/
___/______/______/______/______/______/______/______/______/______/______/______/______/______/______/______/_________/______/______/______/______/______/______/______/______/______/______/______/______/______/______/______/_____
/______/______/______/______/______/______/______/______/______/______/______/______/______/______/______/______/_________/______/______/______/______/______/______/______/______/______/______/______/______/______/______/______/
___/______/______/______/______/______/______/______/______/______/______/______/______/______/______/______/_________/______/______/______/______/______/______/______/______/______/______/______/______/______/______/______/_____
/______/______/______/______/______/______/______/______/______/______/______/______/______/______/______/______/_________/______/______/______/______/______/______/______/______/______/______/______/______/______/______/______/
___/______/______/______/______/______/______/______/______/______/______/______/______/______/______/______/_________/______/______/______/______/______/______/______/______/______/______/______/______/______/______/______/_____
""")



pygame.mixer.music.load(song_menu_inicio)
pygame.mixer.music.play(-1)

while menu_inicio_v==True:

    os.system("cls")
    print(menu_inicio)
    menu_inicio_opc=input(Fore.RESET + "\n\n\n\n\n\n\n\n\n\nEscribe la opción que quieres escoger poniendo su número correspondiente y posteriormente pulsa Enter: ")

    if menu_inicio_opc=="1":
        menu_inicio_v=False
        nombre_personaje=input(Fore.RESET + "\nIntroduce el nombre de tu personaje: ")
        apellido_personaje=input(Fore.RESET + "\nIntroduce el apellido de tu personaje: ")

        break
    elif menu_inicio_opc=="2":
        os.system("cls")
        print(Fore.RESET + """
              
              Este juego tiene dos puntos claves, que son las acciones y los objetos. Vamos a empezar hablando de los objetos.

              Este juego consiste en que, mediente un menú, tu jugador 
              puede realizar diferentes acciones, concretamente estas acciones son:

              1. Coger 
              2. Usar
              3. Dar
              4. Ver Inventario

              Las acciones sirven para interactuar con los objetos, y gracias a la combinación de las acciones y los objetos, podemos resolver los problemas que se nos presentarán en el juego.

              Los objetos se mostrarán en el texto narrativo del texto o en los dibujos ascii que se nos presentan en el juego. 
              
              Para poder realizar las acciones debemos de abrir el menú del juego, este menú se abre dándole a la letra "m" y posteriormente pulsando Enter. 
              Una vez que abrimos el menú, se nos abrirán las las posibles acciones que podemos realizar, es decir, las que hemos mencionado anteriormente arriba.

              Para seleccionar una acción, debemos pulsar dentro del menú, el número de la acción que queremos realizar y posteriormente, pulsar Enter.


_____________________________________________________________________________________________________________________________________
|                                                                                                                                   |
|          Elige la accion que quieres realizar                                                                                     |
|          _      ____                                                          ____      _   _                                     |
|         / |    / ___|___   __ _  ___ _ __                                    |___ \    | | | |___  __ _ _ __                      |
|         | |   | |   / _ \ / _` |/ _ \ '__|                                     __) |   | | | / __|/ _` | '__|                     |
|         | |_  | |__| (_) | (_| |  __/ |                                       / __/ _  | |_| \__ \ (_| | |                        |
|         |_( )  \____\___/ \__, |\___|_|                                      |_____(_) _\___/|___/\__,_|_|                        |
|                            |__ /                                                                                                  |
|          _____    ____                                 _  _     _      _           ___                      _             _       |
|         |___ /   |  _ \  ____ __ _                    | || |    \ \   / /__ _ __  |_ _|_ ____   _____ _ __ | |_ __ _ _ __(_) ___  |
|           |_ \   | | | |/ _` | '__|                   | || |_    \ \ / / _ \ '__|  | || '_ \ \ / / _ \ '_ \| __/ _` | '__| |/ _ \ |
|          ___) |  | |_| | (_| | |                      |__   _|    \ V /  __/ |     | || | | \ V /  __/ | | | || (_| | |  | | (_) ||
|         |____(_) |____/ \__,_|_|                         |_|(_)    \_/ \___|_|    |___|_| |_|\_/ \___|_| |_|\__\__,_|_|  |_|\___/ |  
|                                                                                                                                   |
              

              




              La acción 4, es decir, "Ver inventario", es la única en la que no hay que interactuar con los objetos, es decir, que solamente muestra los objetos que tenemos y nada más.
              En cambio, en el resto de acciones, sí debemos de interactuar con los objetos, veamos cómo.


              

              Coger:

              Estamos dentro del menú y seleccionamos la acción 1, es decir, "coger". 
              A continuación, una vez que hemos entrado en la opción coger, debemos escribir con palabras el objeto que queremos coger, 
              si el objeto que queremos coger, es el correcto, este se guardará automáticamente en nuestro inventario.

              La formula sería: "objeto"

              Ejemplo: papel

              Para volver al menú, pulsamos de nuevo "m" y Enter.

              Recuerda que hay que estar muy atento a los textos y a los dibujos, ya que aquí es donde podemos percibir los objetos que necesitaremos para continuar con la historia.


_____________________________________________________________________________________________________________________________________
|                                                                                                                                   |
|                                                             __                                                                    |
|                                                           / __|___  __ _ ___ _ _                                                  |
|                                                          | (__/ _ \/ _` / -_) '_|                                                 |
|                                                           \___\___/\__, \___|_|                                                   |
|                                                                    |___/                                                          |
|                                                                                                                                   |
|___________________________________________________________________________________________________________________________________|


              

              
              Usar:

              Ahora, estamos dentro del menú y seleccionamos la acción 2 y Enter, es decir, la acción "Usar". 

              Con la opción 2, la opción "usar", podemos podemos combinar dos objetos escribiendo la preposición "con", es decir, escribrimos un objeto, la preposición "con", y el otro objeto con el que lo queremos combinar. 
              
              La opción usar nos permite combinar objetos de nuestro inventario con otros objetos, ya sean de nuestro inventario o fuera de este.

              Fórmula: "objeto" + "con" + "objeto"

              Ejemplo: lápiz con papel 

_____________________________________________________________________________________________________________________________________
|                                                                                                                                   |
|                                                               _   _                                                               |
|                                                              | | | |___ __ _ _ _                                                  |
|                                                              | |_| (_-</ _` | '_|                                                 |
|                                                               \___//__/\__,_|_|                                                   |
|                                                                                                                                   |
|___________________________________________________________________________________________________________________________________|
              
              



              Dar:

              A continuación, volvemos al "menú", dentro del menú y seleccionamos la acción 3 y Enter, es decir, la acción "Dar".

              Esta función sirve para dar un objeto de nuestro inventario a una persona o animal, para ello, una vez que estamos dentro de la acción "Dar", tenemos que escribir el objeto
              de nuestro inventario, seguido de la preposición "a", y la persona o el animal al que le vamos a dar el objeto.

              Fórmula: "objeto" + "a" + "persona / animal"

              Ejemplo: papel a alumno

_____________________________________________________________________________________________________________________________________
|                                                                                                                                   |
|                                                            ___                                                                    |
|                                                           |   \ __ _ _ _                                                          |
|                                                           | |) / _` | '_|                                                         |
|                                                           |___/\__,_|_|                                                           |
|                                                                                                                                   |
|                                                                                                                                   |
|___________________________________________________________________________________________________________________________________|
              


              

              Por último tenemos la opción 4, esta opción, como hemos comentado antes, nos mostrará la lista de objetos de nuestro inventario cuando la seleccionemos, al igual que como en las 
              demás acciones, cuando pulsemos "m" y Enter, volveremos al menú principal.

_____________________________________________________________________________________________________________________________________
|                                                                                                                                   |
|                           ___                 _            _          _        ___  _     _     _                                 |
|                          |_ _|_ ___ _____ _ _| |_ __ _ _ _(_)___   __| |___   / _ \| |__ (_)___| |_ ___ ___                       |
|                           | || ' \ V / -_) ' \  _/ _` | '_| / _ \ / _` / -_) | (_) | '_ \| / -_)  _/ _ (_-<                       |
|                          |___|_||_\_/\___|_||_\__\__,_|_| |_\___/ \__,_\___|  \___/|_.__// \___|\__\___/__/                       |
|                                                                                         |__/                                      |
|___________________________________________________________________________________________________________________________________|
              
            """)
        input("Pulsa Enter para volver al menú principal: ")

        #print(instrucciones)
    elif menu_inicio_opc=="3":
        menu_inicio_v=False
        juego_v=False
        sys.exit()
    else:
        print("Esta opción no está contemplada")


mapa=(Fore.LIGHTGREEN_EX + f"""








                                                                                                        ......==..==.....                             
                                                                                                    .==.                 ..==..                       
                                                                                                 ...                           ...                    
                                                                                              =..                                ..:.                 
                                                                                           .=       N                                 =.               
                                                                                        .-.      O     E                                 .-             
                                                                                        .           S               =                    ...           
                                                                                     ...                        ==={tesoro_unicode}===.                  ...         
                                                                                     =                        :::::{a}:::.                    =.        
                                                                                   .=                         .....{a}......                    =.       
                                                                                  ..                          ....{c}......                     ..      
                                                                                 .=                            =={a}=={cocodrilo_unicode}==                       +      
                                                                                 :           ..                 .{cocodrilo_unicode}===={cocodrilo_unicode}=                      .-     
                                                                                .-         ...::.              ======{d}=====                      =.    
                                                                                :        ....::-======.       ========{d}===:========              .:    
                                                                                =        ....::--==={palmera_unicode}=.     .=========={d}=={arbol_unicode} ====--:            +.   
                                                                               ..        ........{palmera_unicode}.{serpiente_unicode}{palmera_unicode}{b}{b}{b}{b}{b}{b}{b}{b}{b}{b}{b}{b}{b}{b}{b}{b}{b}{casa_unicode}  ={arbol_unicode}::...            . .   
                                                                               :.        .....{palmera_unicode}{tigre_unicode}.{palmera_unicode}....== =:============--::.                  .-   
                                                                               ..         .......{palmera_unicode}..{palmera_unicode}..    ...:.:::::...                       ..   
                                                                               ..          .........{a}.....      .....                            ..   
                                                                                .          .........{a}.....                                       ..   
                                                                                =          ..........{d}.:--                                      .+    
                                                                                .           .....:--= {cabaña_unicode}  ====                                  ..    
                                                                                 =         ...::-== {cabaña_unicode}   {fuego_unicode} {moai_unicode}==                               .+     
                                                                                 ..         .::-===   {cabaña_unicode}   =+                                 ..     
                                                                                  ..        .::-:====={a}====                                   ..      
                                                                                   ..        ..::-==={c}======                                 ..       
                                                                                    =.       .....::{a}-====                                 .=        
                                                                                     .=        .....{playa_unicode}....           
                                                                                       -.       ...   ..                                  .-.          
                                                                                        .=                                                  
                                                                                         ..=                                          =.              
                                                                                             =..                                  ..=..               
                                                                                               .:..                            ..-.                   
                                                                                                   .==..                    ==..                      
                                                                                                        .:==..........==- .                           
                                                                                                                                                      """)

mapa_menu=(f"""


                                                                                {Fore.LIGHTWHITE_EX} __  __                         _        _         _     _       
                                                                                |  \/  |                       | |      | |       (_)   | |      
                                                                                | \  / | __ _ _ __   __ _    __| | ___  | | __ _   _ ___| | __ _ 
                                                                                | |\/| |/ _` | '_ \ / _` |  / _` |/ _ \ | |/ _` | | / __| |/ _` |
                                                                                | |  | | (_| | |_) | (_| | | (_| |  __/ | | (_| | | \__ \ | (_| |
                                                                                |_|  |_|\__,_| .__/ \__,_|  \__,_|\___| |_|\__,_| |_|___/_|\__,_|
                                                                                             | |                                                 
                                                                                             |_|{Fore.LIGHTGREEN_EX}                                                      



      
                                                                    
                                                                                                        ......==..==.....                             
                                                                                                    .==.                 ..==..                       
                                                                                                 ...                           ...                    
                                                                                              =..                                ..:.                 
                                                                                           .=       N                                 =.               
                                                                                        .-.      O     E                                 .-             
                                                                                        .           S               =                    ...           
                                                                                     ...                        ==={tesoro_unicode}===.                  ...         
                                                                                     =                        :::::{a}:::.                    =.        
                                                                                   .=                         .....{a}......                    =.       
                                                                                  ..                          ....{c}......                     ..      
                                                                                 .=                            =={a}=={cocodrilo_unicode}==                       +      
                                                                                 :           ..                 .{cocodrilo_unicode}===={cocodrilo_unicode}=                      .-     
                                                                                .-         ...::.              ======{d}=====                      =.    
                                                                                :        ....::-======.       ========{d}===:========              .:    
                                                                                =        ....::--==={palmera_unicode}=.     .=========={d}=={arbol_unicode} ====--:            +.   
                                                                               ..        ........{palmera_unicode}.{serpiente_unicode}{palmera_unicode}{b}{b}{b}{b}{b}{b}{b}{b}{b}{b}{b}{b}{b}{b}{b}{b}{b}{casa_unicode}  ={arbol_unicode}::...            . .   
                                                                               :.        .....{palmera_unicode}{tigre_unicode}.{palmera_unicode}....== =:============--::.                  .-   
                                                                               ..         .......{palmera_unicode}..{palmera_unicode}..    ...:.:::::...                       ..   
                                                                               ..          .........{a}.....      .....                            ..   
                                                                                .          .........{a}.....                                       ..   
                                                                                =          ..........{d}.:--                                      .+    
                                                                                .           .....:--= {cabaña_unicode}  ====                                  ..    
                                                                                 =         ...::-== {cabaña_unicode}   {fuego_unicode} {moai_unicode}==                               .+     
                                                                                 ..         .::-===   {cabaña_unicode}   =+                                 ..     
                                                                                  ..        .::-:====={a}====                                   ..      
                                                                                   ..        ..::-==={c}======                                 ..       
                                                                                    =.       .....::{a}-====            MAPA DEL TESORO       .=        
                                                                                     .=        .....{playa_unicode}....           
                                                                                       -.       ...   ..                                  .-.          
                                                                                        .=                                  J. {apellido_personaje}                
                                                                                         ..=                                          =.              
                                                                                             =..                                  ..=..               
                                                                                               .:..                            ..-.                   
                                                                                                   .==..                    ==..                      
                                                                                                        .:==..........==- .                           
                                                                                                                                                      """)

pygame.mixer.music.stop()

os.system("cls")

texto1=Fore.RESET + f"""
\n\n\n\n\n\n
\t\t\t\t\t\t\t\t\t\t\t\tNos encontramos a principios del siglo XVIII, 
\t\t\t\t\t\t\t\t\t\t\t\tante la asombrosa aventura del pirata {nombre_personaje} {apellido_personaje},
\t\t\t\t\t\t\t\t\t\t\t\tun intrépido pero desvergonzado pirata que surca los mares
\t\t\t\t\t\t\t\t\t\t\t\tcon el fin de saquear, beber y fornicar en cada puerto en el que desembarque, 
\t\t\t\t\t\t\t\t\t\t\t\tsu único fin es no acabar desaparecido o encarcelado como lo fue su padre, 
\t\t\t\t\t\t\t\t\t\t\t\tel ser pirata parece que se transmite por sangre…

\t\t\t\t\t\t\t\t\t\t\t\tDespués de haberse jugado el pescuezo y haber burlado a la autoridad
\t\t\t\t\t\t\t\t\t\t\t\tde Bangkok, tras saquear todo el ron que tenían en una fábrica, 
\t\t\t\t\t\t\t\t\t\t\t\tsubió a su barco para seguir con su viaje sin rumbo, para ver que 
\t\t\t\t\t\t\t\t\t\t\t\tle deparaba su próximo destino.

\t\t\t\t\t\t\t\t\t\t\t\tA continuación, procedió a abrir una de las botellas de ron, 
\t\t\t\t\t\t\t\t\t\t\t\ttumbarse en su camarote, y disfrutar de una buena borrachera, 
\t\t\t\t\t\t\t\t\t\t\t\tcelebrando una vez más que no lo habían pillado. 

\t\t\t\t\t\t\t\t\t\t\t\tDe repente, tú, {nombre_personaje} {apellido_personaje}, te despiertas borracho perdido,
\t\t\t\t\t\t\t\t\t\t\t\tno sabes que está pasando, si el alcohol hace que no puedas
\t\t\t\t\t\t\t\t\t\t\t\tmantenerte en pie, o es que hay un tifón del pacífico que hace 
\t\t\t\t\t\t\t\t\t\t\t\tque el barco se mueva como una maraca. En ese momento vas hacia 
\t\t\t\t\t\t\t\t\t\t\t\tla ventana, y por desgracia, está ocurriendo lo segundo.

\t\t\t\t\t\t\t\t\t\t\t\tJusto en ese momento, parece que algo grande y voluminoso está
\t\t\t\t\t\t\t\t\t\t\t\tcobrando vida y se acerca hacia el barco con una fuerza.
\t\t\t\t\t\t\t\t\t\t\t\tEfectivamente, era una ola.

\t\t\t\t\t\t\t\t\t\t\t\tPulsa Enter para continuar
"""
texto_tribu=(Fore.RESET + """
\n\n\n\n\n\n\n\n\n\n
\t\t\t\t\t\t\t\t\t\t\t  ¡CARAY! Nos hemos adentrado en la vegetación en busca de una salida 
\t\t\t\t\t\t\t\t\t\t\t  y nos hemos topado con una tribu indígena, no parecen peligrosos 
\t\t\t\t\t\t\t\t\t\t\t  a pesar de llevar lanzas, cuchillos y una hoguera gigante a la que le 
\t\t\t\t\t\t\t\t\t\t\t  están bailando, ¡vaya! parece que el jefe de la tribu se está acercando,
\t\t\t\t\t\t\t\t\t\t\t  a ver si él nos puede ayudar...
""")

texto_padre=(Fore.RESET + f"""
\n\n\n\n\n\n
\t\t\t\t\t\t\t\t\t\t\t\tLlevo atrapado en esta isla mucho tiempo, 
\t\t\t\t\t\t\t\t\t\t\t\tme siento vacio, ya que solo he conocido
\t\t\t\t\t\t\t\t\t\t\t\ta unos indígenas que han intentado comerme,
\t\t\t\t\t\t\t\t\t\t\t\tmenos mal que me quedaba una botella de ron
\t\t\t\t\t\t\t\t\t\t\t\ty los pude emborrachar.
\n\t\t\t\t\t\t\t\t\t\t\t\tEcho de menos a mi hijo, tenía que haber 
\t\t\t\t\t\t\t\t\t\t\t\tdejado la vida de pirata y haberme quedado 
\t\t\t\t\t\t\t\t\t\t\t\tcon él.
\n\t\t\t\t\t\t\t\t\t\t\t\tPero... no todo está perdido, acabo de 
\t\t\t\t\t\t\t\t\t\t\t\tdescubrir este mapa del tesoro, que me hará 
\t\t\t\t\t\t\t\t\t\t\t\trico y me permitirá dejar esta vida de
\t\t\t\t\t\t\t\t\t\t\t\tpirata además de volver con mi hijo.
\t\t\t\t\t\t\t\t\t\t\t\tPor fin podré tener una vida tranquila...
\t\t\t\t\t\t\t\t\t\t\t\tLo único que tengo que hacer es burlar
\t\t\t\t\t\t\t\t\t\t\t\ta esa enorme bestia del pantano y podré
\t\t\t\t\t\t\t\t\t\t\t\tllegar al tesoro.
\n\t\t\t\t\t\t\t\t\t\t\t\tJuro, como que me llamo Jhon {apellido_personaje},
\t\t\t\t\t\t\t\t\t\t\t\tque me haré con el tesoro y 
\t\t\t\t\t\t\t\t\t\t\t\tvolveré con mi hijo {nombre_personaje}""")


pygame.mixer.music.load(song_inicio_pirata)
pygame.mixer.music.play(-1)


for _ in texto1:
    print(_, end="", flush=True)
    
    if _!="\t" and "\n":
        time.sleep(0.04)

input()


pygame.mixer.music.stop()

os.system("cls")   

pygame.mixer.music.load(sonido_barco_olas)
pygame.mixer.music.play()


for i in range (20):
   
   mar_b=" " *i
   mar_a=(19-i)*" "
   mar_c="@"*i

   barco=(Fore.RESET + f"""                                                                                                             

                                                                                                                                                                 .%...                           
                                                                                                                                                                 .@%%%%%%%.... .-=..               
                                                                                                                                                                ..@...   ..:...                  
                                                                                                                                                                %%%@..                           
                                                                                                                                                              ...=@..                            
                                                                                                                                                           .%%%%%@%%%%%%%.                       
                                                                                                                                                          .%%%%%%%%%%%%%%.                       
                                                                                                                                                        ..@%%%%%%%%%%%%%%..                      
                                                                                                                                                        .+%%%%%%%%%%%%%%%%.                      
                                                                                                                                                        .#%%%%%%%%%%%%%%%%%.                     
                                                                                                                                                        ..%%%%@@@%%%@%%%%%%@..                   
                                                                                                                                      ..          ...............=%.....................         
                                                                                                                                     @@@.         ..%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%..            
                                                                                                                                  #%%%%%%%%%      .%%%%%%%%%#....   ....%%%%%%%%%%%%%..          
                                                                                                                                .%%%%%%%%%%+     .%%%%%%%%@..           .-%%%%%%%%%%.            
                                                                                                                                +%%%%%%%%%%%..   *%%%%%%%%%.             .%%%%%%%%%.             
                                                                                                                                %%%%%%%%%%%%%.   %%%%%%%%%@..            %%%%%%%%%@.           .:
                                                                                                                                .@*...@=...:*#:.:%%#%###%%%#*#%%%..=%%%% ###%%#%%%.      ..   .*%
                                                                                                                             .+%%%%%%%%%#%%#%%@+#%%%%%%%%%%%.=%%=:..*%#.-%%%%%%%%@.     ..%.. %%%
                                                                                                                            .%%%%%%%%%%#%%@%@-..#%%%%%%%%%%%%.%:.:...--=%%%%%%%%%.       .%.%%%%@
                                                                                                                           .%%%%%%%%%%@#%####.:.@%@#%#####%##+=.=%+..+.#%%%%%%%%%.       .%%%%%%%..
                                                      {Fore.BLUE}{mar_b}.@@@@*.. . *@@@@.{Fore.RESET}                           {mar_a}       %%%%%%%%%%%%%%%%%. .%%%%%%%@..%%%%...#+....%%%@.:%%%%.      .-%%%%%%%-.
                                                   {Fore.BLUE}{mar_b}@@@     @@@@@@@@.   @@{Fore.RESET}                          {mar_a}      %%%%%%%%%%%%%%%%@. .@%%%%%%@...-@%%%:...=%%%%...:%%%@      .#%%%%%%%%@.
                                                {Fore.BLUE}{mar_b}%@:  @@                  @# :{Fore.RESET}                   {mar_a}         %%%%%%%%%%%%%%%%%= .%%%%%%%#.-%:....-%%%.....+%..%%%@      %%%%%%%%%%%.
                                             {Fore.BLUE}{mar_b}@@  @-                       .@@{Fore.RESET}                {mar_a}....       =%%%%%%%%%%%%%%%%@..:%%%%%%%%%%%%@*.....+@%%%%%%%%%%@.   .%%%%%%%#-.....
                                          {Fore.BLUE}{mar_b}@@                                 @@{Fore.RESET}              {mar_a}..:%@:.  ..@%%%@%%%%%%%%%%%%...%%%%@.........*@%%@%-........:%%.  .@%+..%.. ..#@%. 
                                          {Fore.BLUE}{mar_b}#@                                  @{Fore.RESET}                   {mar_a}...#%@@=.. .    @=... .*+  %%%%%%.  *%@%%%%%%%%%%@@%.  *%%%  ....  .%@%%%%%%%%
                                       {Fore.BLUE}{mar_b}.@                           -@  @     @{Fore.RESET}               {mar_a}     .%%%%%%%%%%@%@%@=..........%%%%%*.*%%%%%@%%%%%%%%@%%..%%%%- .*@%%%%%%%%%%%%%%..
                                       {Fore.BLUE}{mar_b}@-                         .@     @  @{Fore.RESET}                      {mar_a}.%%%%%%%%%-..%%%%%%%%%%%%%+..@%%%@%#-..... =%.. .   ....:*@%..@%%%%%%%%%%%%%..
                                    {Fore.BLUE}{mar_b}.@@    QOOOOQ                @@{Fore.RESET}                            {mar_a}     %%%%%%%%%@. @%%%%%%%%%%%%%%..@.           =%.            ..#%%%%%%%%%%%%%#
                                 {Fore.BLUE}{mar_b}.@+     OYZZXPPRYYO            .@{Fore.RESET}                              {mar_a} ..@@*:...:*%@.:%%%%%%%%%%%%%%%@%.           =%.         ..@@@%%%%%%%%%%%%@=.
                              {Fore.BLUE}{mar_b}@@.  @   OZZPOOOOP   QO           @@{Fore.RESET}                               {mar_a}                 ..%%%%%%%%%%%%%%%%%%%%%@+......=%...:#@%%%%%%%%%%%%%%%%%%%%%
                           {Fore.BLUE}{mar_b}@@@  .@   QTZYOOOOO                  .@{Fore.RESET}                                {mar_a}                   @%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%+
                        {Fore.BLUE}{mar_b}.@@%   @    OZZOOOOOOO                    @{Fore.RESET}                                {mar_a}                   .%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%@%. 
                     {Fore.BLUE}{mar_b}.@@   @@     NPZPOOOOOOOOX                      @@{Fore.RESET}                              {mar_a}                   .#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%.
                  {Fore.BLUE}{mar_b}.@@@@@:        OQOOOOOOOOOOOOP       @               @@@:{Fore.RESET}                           {mar_a}                    .+%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%*...
               {Fore.BLUE}{mar_b}.@@@@@*.      QOOOOOOOOOOOOOOOOOOOOOOP                       .@@@@@@@@@@@#.{Fore.RESET}         {mar_a}                           .%%%@%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%@%%@..
{Fore.BLUE}@@@@{mar_c}@@@@@@@@@@@@@@=              @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@""")
   
   print(barco)
   time.sleep(0.2)
   os.system("cls")

pygame.mixer.music.stop()   
pygame.mixer.music.stop()


pygame.mixer.music.load(sonido_pum)
pygame.mixer.music.play()

print(f"""{Fore.RESET}\n\n\n\n\n\n\n\n\n\n\n\n
\t\t\t\t\t\t\t\t\t\t\t\t                                ,---.,---.,---.
\t\t\t\t\t\t\t\t\t\t\t\t,------. ,--. ,--.,--.   ,--.   |   ||   ||   |
\t\t\t\t\t\t\t\t\t\t\t\t|  .--. '|  | |  ||   `.'   |   |  .'|  .'|  .'
\t\t\t\t\t\t\t\t\t\t\t\t|  '--' ||  | |  ||  |'.'|  |   |  | |  | |  | 
\t\t\t\t\t\t\t\t\t\t\t\t|  | --' '  '-'  '|  |   |  |   `--' `--' `--' 
\t\t\t\t\t\t\t\t\t\t\t\t`--'      `-----' `--'   `--'   .--. .--. .--. 
\t\t\t\t\t\t\t\t\t\t\t\t                                '--' '--' '--' """)

time.sleep(2)

pygame.mixer.music.stop()

pygame.mixer.music.load(song_playa)
pygame.mixer.music.play(-1)

while playa_v==True:


  os.system("cls")
  


  print(f"""                          {Fore.GREEN}#####
                        #######                                                                                                                     {Fore.LIGHTWHITE_EX}Has naufragado en una playa y no sabes dónde te encuentras.{Fore.GREEN}
              ######    ########       #####                                                                                                  
          ###########/#####\#####  #############                                                                                                    {Fore.LIGHTWHITE_EX}A continuación vamos a ver cómo funcionan los controles.{Fore.GREEN}
      ############/##########--#####################
    ####         ######################          #####                                                                                              {Fore.LIGHTWHITE_EX}Comienza pulsando 'm' y después Enter para abrir el menú{Fore.GREEN}
  ##          ####      ##########/@@              ###
  #          ####        ,-.##/`.#\#####               ##
            ###        {Fore.YELLOW} /  |./  |,-. {Fore.GREEN}####                 #
          ##           {Fore.YELLOW}\_,'\_,'|  \  {Fore.GREEN}###
          #             {Fore.YELLOW}\_{Fore.LIGHTBLACK_EX}$$$$${Fore.YELLOW}`._/   {Fore.GREEN}##   
                          {Fore.LIGHTBLACK_EX}$$$$${Fore.YELLOW}_/     {Fore.GREEN}# {Fore.LIGHTBLACK_EX}    
                          $$$$$        
                          $$$$$
                          $$$$$
                         $$$$$
                        $$$$$
                        $$$$$
                        $$$$$
                        $$$$$
                        $$$$$         ___
                        $$$$$     _.-'   `-._
                        $$$$$   ,'           `.
                        $$$$$  /               '
~~~~~~~~~~~~~~~~~~~~~~~$$$$$~~~'~~~~~~~~~~~~~~~~`~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~{Back.BLACK}                                                                     
{Back.BLUE}   ~      ~  ~    ~  ~ {Back.BLACK}{Fore.LIGHTBLACK_EX}$$$$${Back.BLUE}  ~   ~       ~          ~                                                                                {Back.BLACK}
{Back.BLUE}       ~               {Back.BLACK}{Fore.LIGHTBLACK_EX}$$$$${Back.BLUE}     ~    ~          ~                                                                                    {Back.BLACK}
{Back.BLUE}  ~            ~    ~  {Back.BLACK}{Fore.LIGHTBLACK_EX}$$$$${Back.BLUE}~                     ~        ~                                                                          {Back.BLACK}
{Back.BLUE}                       {Back.BLACK}{Fore.LIGHTBLACK_EX}$$$$${Back.BLUE}                                                                                                          {Back.BLACK}
{Back.LIGHTYELLOW_EX}                       {Back.BLACK}{Fore.LIGHTBLACK_EX}$$$$${Back.LIGHTYELLOW_EX}                                                                                                          {Back.BLACK}
{Back.LIGHTYELLOW_EX}                       {Back.BLACK}{Fore.LIGHTBLACK_EX}$$$$${Back.LIGHTYELLOW_EX}                                                                                                          {Back.BLACK}
{Back.LIGHTYELLOW_EX}                       {Back.BLACK}{Fore.LIGHTBLACK_EX}$$$$${Back.LIGHTYELLOW_EX}    {Fore.BLACK}_      .                                                                                              {Back.BLACK}
{Back.LIGHTYELLOW_EX}                       {Back.BLACK}{Fore.LIGHTBLACK_EX}$$$$${Back.LIGHTYELLOW_EX}    {Fore.BLACK}\`-- -´|                                                                                              {Back.BLACK}
{Back.LIGHTYELLOW_EX}                      {Back.BLACK}{Fore.LIGHTBLACK_EX}$$$$$$${Back.LIGHTYELLOW_EX}    {Fore.BLACK}`----'                                                                                               {Back.BLACK}
{Back.LIGHTYELLOW_EX}                      {Back.BLACK}{Fore.LIGHTBLACK_EX}$$$$$$${Back.LIGHTYELLOW_EX}    {Fore.BLACK}banana                                                                                               {Back.BLACK}
{Back.LIGHTYELLOW_EX}                     {Back.BLACK}{Fore.LIGHTBLACK_EX}$$$$$$$$${Back.LIGHTYELLOW_EX}                                                                                                        {Back.BLACK}
{Back.LIGHTYELLOW_EX}                     {Back.BLACK}{Fore.LIGHTBLACK_EX}$$$$$$$$${Back.BLACK}
  """)




  opc_menu=input("\n\n" + Fore.LIGHTWHITE_EX + "       --> ").lower()
  
  if opc_menu!="m":
    print(Fore.LIGHTWHITE_EX, "Esta opción no está contemplada")
    input()




  if opc_menu=="m":
    
    os.system("cls")

    print(f"""


                          {Fore.GREEN}#####
                        #######                                                                                                                  {Fore.LIGHTWHITE_EX}Se te acaba de abrir un menú, y tienes las siguientes opciones:{Fore.GREEN}
              ######    ########       #####                                                                                                  
          ###########/#####\#####  #############                                                                                                    {Fore.LIGHTWHITE_EX}1. Coger{Fore.GREEN}
      ############/##########--#####################                                                                                                {Fore.LIGHTWHITE_EX}2. Usar{Fore.GREEN}
    ####         ######################          #####                                                                                              {Fore.LIGHTWHITE_EX}3. Dar{Fore.GREEN}
  ##          ####      ##########/@@              ###                                                                                              {Fore.LIGHTWHITE_EX}4. Ver inventario{Fore.GREEN}
  #          ####        ,-.##/`.#\#####               ##
            ###        {Fore.YELLOW} /  |./  |,-. {Fore.GREEN}####                 #                                                                                      {Fore.LIGHTWHITE_EX}Entre las acciones y los objetos, podemos hacer múltiples funciones como son:{Fore.GREEN}
          ##           {Fore.YELLOW}\_,'\_,'|  \  {Fore.GREEN}###
          #             {Fore.YELLOW}\_{Fore.LIGHTBLACK_EX}$$$$${Fore.YELLOW}`._/   {Fore.GREEN}##                                                                                                            {Fore.LIGHTWHITE_EX}1. Coger{Fore.GREEN}
                          {Fore.LIGHTBLACK_EX}$$$$${Fore.YELLOW}_/     {Fore.GREEN}# {Fore.LIGHTBLACK_EX}                                                                                                            {Fore.LIGHTWHITE_EX}2. Usar{Fore.LIGHTBLACK_EX}   
                          $$$$$                                                                                                                     {Fore.LIGHTWHITE_EX}3. Dar{Fore.LIGHTBLACK_EX}    
                          $$$$$
                          $$$$$                                                                                                                  {Fore.LIGHTWHITE_EX}Para poder interactuar con un objeto, hay que pulsar el número que{Fore.LIGHTBLACK_EX} 
                         $$$$$                                                                                                                   {Fore.LIGHTWHITE_EX}corresponde a esa acción y posteriormente pulsar el boton Enter.{Fore.LIGHTBLACK_EX} 
                         $$$$$                                                                                                                   {Fore.LIGHTWHITE_EX}Una vez que hemos entrado en el menu de la accion solo tenemos que{Fore.LIGHTBLACK_EX} 
                        $$$$$                                                                                                                    {Fore.LIGHTWHITE_EX}escribir el objeto con el que vamos a interactuar, excepto en la opción 4.{Fore.LIGHTBLACK_EX}
                        $$$$$                                                                                                       
                        $$$$$                                                                                                                    {Fore.LIGHTWHITE_EX}Para probar que lo hemos entendido, prueba a {Fore.RED}ver el inventario{Fore.LIGHTBLACK_EX}
                        $$$$$         ___                                                                                                        {Fore.LIGHTWHITE_EX}pulsando {Fore.RED}4 y Enter{Fore.LIGHTBLACK_EX} 
                        $$$$$     _.-'   `-._
                        $$$$$   ,'           `.
                        $$$$$  /               '
~~~~~~~~~~~~~~~~~~~~~~~$$$$$~~~'~~~~~~~~~~~~~~~~`~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~{Back.BLACK}                                                                     
{Back.BLUE}   ~      ~  ~    ~  ~ {Back.BLACK}{Fore.LIGHTBLACK_EX}$$$$${Back.BLUE}  ~   ~       ~          ~                                                                                {Back.BLACK}                                                                               
{Back.BLUE}       ~               {Back.BLACK}{Fore.LIGHTBLACK_EX}$$$$${Back.BLUE}     ~    ~          ~                                                                                    {Back.BLACK}                                                                                           
{Back.BLUE}  ~            ~    ~  {Back.BLACK}{Fore.LIGHTBLACK_EX}$$$$${Back.BLUE}~                     ~        ~                                                                          {Back.BLACK}                                                                                
{Back.BLUE}                       {Back.BLACK}{Fore.LIGHTBLACK_EX}$$$$${Back.BLUE}                                                                                                          {Back.BLACK}                                                                                      
{Back.LIGHTYELLOW_EX}                       {Back.BLACK}{Fore.LIGHTBLACK_EX}$$$$${Back.LIGHTYELLOW_EX}                                                                                                          {Back.BLACK}                                                                                 
{Back.LIGHTYELLOW_EX}                       {Back.BLACK}{Fore.LIGHTBLACK_EX}$$$$${Back.LIGHTYELLOW_EX}                                                                                                          {Back.BLACK}                                                                                   
{Back.LIGHTYELLOW_EX}                       {Back.BLACK}{Fore.LIGHTBLACK_EX}$$$$${Back.LIGHTYELLOW_EX}    {Fore.BLACK}_      .                                                                                              {Back.BLACK}                                                                                    
{Back.LIGHTYELLOW_EX}                       {Back.BLACK}{Fore.LIGHTBLACK_EX}$$$$${Back.LIGHTYELLOW_EX}    {Fore.BLACK}\`-- -´|                                                                                              {Back.BLACK}                                                                                  
{Back.LIGHTYELLOW_EX}                      {Back.BLACK}{Fore.LIGHTBLACK_EX}$$$$$$${Back.LIGHTYELLOW_EX}    {Fore.BLACK}`----'                                                                                               {Back.BLACK}                                                                                 
{Back.LIGHTYELLOW_EX}                      {Back.BLACK}{Fore.LIGHTBLACK_EX}$$$$$$${Back.LIGHTYELLOW_EX}    {Fore.BLACK}banana                                                                                               {Back.BLACK}                                                                                
{Back.LIGHTYELLOW_EX}                     {Back.BLACK}{Fore.LIGHTBLACK_EX}$$$$$$$$${Back.LIGHTYELLOW_EX}                                                                                                        {Back.BLACK}                                                                                  
{Back.LIGHTYELLOW_EX}                     {Back.BLACK}{Fore.LIGHTBLACK_EX}$$$$$$$$${Back.BLACK}
  """)
  


    
    print(acciones)
    opc_playa=input("|       --> ")
    
    if opc_playa!="4":
      print(Fore.LIGHTWHITE_EX, "Esta opción no está contemplada")
      input()




    while opc_playa=="4":
      os.system("cls")


      print(f"""                          {Fore.GREEN}#####
                        #######                                                                                                                                {Fore.LIGHTWHITE_EX}¡Vaya!, Parece que ya teníamos algunos objetos recolectados{Fore.GREEN}
              ######    ########       #####                                                                                                  
          ###########/#####\#####  #############                                                                                                               {Fore.LIGHTWHITE_EX}Ahora, vuelve al menú de acciones pulsando "m"{Fore.GREEN}
      ############/##########--#####################
    ####         ######################          #####                                                                                                         {Fore.LIGHTWHITE_EX}para ver que más podemos hacer.{Fore.GREEN}
  ##          ####      ##########/@@              ###
  #          ####        ,-.##/`.#\#####               ##
            ###        {Fore.YELLOW} /  |./  |,-. {Fore.GREEN}####                 #
          ##           {Fore.YELLOW}\_,'\_,'|  \  {Fore.GREEN}###
          #             {Fore.YELLOW}\_{Fore.LIGHTBLACK_EX}$$$$${Fore.YELLOW}`._/   {Fore.GREEN}##   
                          {Fore.LIGHTBLACK_EX}$$$$${Fore.YELLOW}_/     {Fore.GREEN}# {Fore.LIGHTBLACK_EX}    
                          $$$$$        
                          $$$$$
                          $$$$$
                          $$$$$
                         $$$$$
                        $$$$$
                        $$$$$
                        $$$$$
                        $$$$$        ___
                        $$$$$    _.-'   `-._
                        $$$$$   ,'           `.
                        $$$$$  /               '
~~~~~~~~~~~~~~~~~~~~~~~$$$$$~~~'~~~~~~~~~~~~~~~~`~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~{Back.BLACK}                                                                     
{Back.BLUE}   ~      ~  ~    ~  ~ {Back.BLACK}{Fore.LIGHTBLACK_EX}$$$$${Back.BLUE}  ~   ~       ~          ~                                                                                {Back.BLACK}                                                                               
{Back.BLUE}       ~               {Back.BLACK}{Fore.LIGHTBLACK_EX}$$$$${Back.BLUE}     ~    ~          ~                                                                                    {Back.BLACK}                                                                                           
{Back.BLUE}  ~            ~    ~  {Back.BLACK}{Fore.LIGHTBLACK_EX}$$$$${Back.BLUE}~                     ~        ~                                                                          {Back.BLACK}                                                                             
{Back.BLUE}                       {Back.BLACK}{Fore.LIGHTBLACK_EX}$$$$${Back.BLUE}                                                                                                          {Back.BLACK}                                                                                          
{Back.LIGHTYELLOW_EX}                       {Back.BLACK}{Fore.LIGHTBLACK_EX}$$$$${Back.LIGHTYELLOW_EX}                                                                                                          {Back.BLACK}                                                                                          
{Back.LIGHTYELLOW_EX}                       {Back.BLACK}{Fore.LIGHTBLACK_EX}$$$$${Back.LIGHTYELLOW_EX}                                                                                                          {Back.BLACK}                                                                                          
{Back.LIGHTYELLOW_EX}                       {Back.BLACK}{Fore.LIGHTBLACK_EX}$$$$${Back.LIGHTYELLOW_EX}    {Fore.BLACK}_      .                                                                                              {Back.BLACK}                                                                                          
{Back.LIGHTYELLOW_EX}                       {Back.BLACK}{Fore.LIGHTBLACK_EX}$$$$${Back.LIGHTYELLOW_EX}    {Fore.BLACK}\`-- -´|                                                                                              {Back.BLACK}                                                                                          
{Back.LIGHTYELLOW_EX}                      {Back.BLACK}{Fore.LIGHTBLACK_EX}$$$$$$${Back.LIGHTYELLOW_EX}    {Fore.BLACK}`----'                                                                                               {Back.BLACK}                                                                                          
{Back.LIGHTYELLOW_EX}                      {Back.BLACK}{Fore.LIGHTBLACK_EX}$$$$$$${Back.LIGHTYELLOW_EX}    {Fore.BLACK}banana                                                                                               {Back.BLACK}                                                                                          
{Back.LIGHTYELLOW_EX}                     {Back.BLACK}{Fore.LIGHTBLACK_EX}$$$$$$$$${Back.LIGHTYELLOW_EX}                                                                                                        {Back.BLACK}                                                                                          
{Back.LIGHTYELLOW_EX}                     {Back.BLACK}{Fore.LIGHTBLACK_EX}$$$$$$$$${Back.BLACK}
  """)
        
      print(inventario_intf)

      for i in list(objetos):
          contador_objetos+=1
          print(contador_objetos, objetos[contador_objetos-1])
      contador_objetos=0

      opc_menu=input("\n\n   --> ").lower()

      if opc_menu!="m":
        print(Fore.LIGHTWHITE_EX, "Esta opción no está contemplada")
        input()


        

      while opc_menu=="m":
        os.system("cls")



        print(f"""                          {Fore.GREEN}#####
                        #######                                                                                                              
              ######    ########       #####                                                                                                                          {Fore.LIGHTWHITE_EX}Ahora prueba a usar el palo con las cerillas{Fore.GREEN}
          ###########/#####\#####  #############                                                                                              
      ############/##########--#####################                                                                                                                  {Fore.LIGHTWHITE_EX}Para ello, pulsa el {Fore.RED}2{Fore.LIGHTWHITE_EX}, la opción usar.{Fore.GREEN}
    ####         ######################          #####                                                                                        
  ##         ###      ##########/@@              ###                                                                                                                 
  #          ####        ,-.##/`.#\#####               ##
            ###        {Fore.YELLOW} /  |./  |,-. {Fore.GREEN}####                 #
          ##           {Fore.YELLOW}\_,'\_,'|  \  {Fore.GREEN}###
          #             {Fore.YELLOW}\_{Fore.LIGHTBLACK_EX}$$$$${Fore.YELLOW}`._/   {Fore.GREEN}##   
                          {Fore.LIGHTBLACK_EX}$$$$${Fore.YELLOW}_/     {Fore.GREEN}# {Fore.LIGHTBLACK_EX}    
                          $$$$$        
                          $$$$$
                          $$$$$
                          $$$$$
                         $$$$$
                        $$$$$
                        $$$$$
                        $$$$$
                        $$$$$        ___
                        $$$$$    _.-'   `-._
                        $$$$$   ,'           `.
                        $$$$$  /               '
~~~~~~~~~~~~~~~~~~~~~~~$$$$$~~~'~~~~~~~~~~~~~~~~`~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~{Back.BLACK}                                                                     
{Back.BLUE}   ~      ~  ~    ~  ~ {Back.BLACK}{Fore.LIGHTBLACK_EX}$$$$${Back.BLUE}  ~   ~       ~          ~                                                                                {Back.BLACK}                                                                               
{Back.BLUE}       ~               {Back.BLACK}{Fore.LIGHTBLACK_EX}$$$$${Back.BLUE}     ~    ~          ~                                                                                    {Back.BLACK}                                                                                           
{Back.BLUE}  ~            ~    ~  {Back.BLACK}{Fore.LIGHTBLACK_EX}$$$$${Back.BLUE}~                     ~        ~                                                                          {Back.BLACK}                                                                            
{Back.BLUE}                       {Back.BLACK}{Fore.LIGHTBLACK_EX}$$$$${Back.BLUE}                                                                                                          {Back.BLACK}                                                                                        
{Back.LIGHTYELLOW_EX}                       {Back.BLACK}{Fore.LIGHTBLACK_EX}$$$$${Back.LIGHTYELLOW_EX}                                                                                                          {Back.BLACK}                                                                                        
{Back.LIGHTYELLOW_EX}                       {Back.BLACK}{Fore.LIGHTBLACK_EX}$$$$${Back.LIGHTYELLOW_EX}                                                                                                          {Back.BLACK}                                                                                        
{Back.LIGHTYELLOW_EX}                       {Back.BLACK}{Fore.LIGHTBLACK_EX}$$$$${Back.LIGHTYELLOW_EX}    {Fore.BLACK}_      .                                                                                              {Back.BLACK}                                                                                        
{Back.LIGHTYELLOW_EX}                       {Back.BLACK}{Fore.LIGHTBLACK_EX}$$$$${Back.LIGHTYELLOW_EX}    {Fore.BLACK}\`-- -´|                                                                                              {Back.BLACK}                                                                                        
{Back.LIGHTYELLOW_EX}                      {Back.BLACK}{Fore.LIGHTBLACK_EX}$$$$$$${Back.LIGHTYELLOW_EX}    {Fore.BLACK}`----'                                                                                               {Back.BLACK}                                                                                        
{Back.LIGHTYELLOW_EX}                      {Back.BLACK}{Fore.LIGHTBLACK_EX}$$$$$$${Back.LIGHTYELLOW_EX}    {Fore.BLACK}banana                                                                                               {Back.BLACK}                                                                                        
{Back.LIGHTYELLOW_EX}                     {Back.BLACK}{Fore.LIGHTBLACK_EX}$$$$$$$$${Back.LIGHTYELLOW_EX}                                                                                                        {Back.BLACK}                                                                                        
{Back.LIGHTYELLOW_EX}                     {Back.BLACK}{Fore.LIGHTBLACK_EX}$$$$$$$$${Back.BLACK}
    """)
    
        print(acciones)
        opc_playa=input("|       --> ")

        if opc_playa!="2":
          print(Fore.LIGHTWHITE_EX, "Esta opción no está contemplada")
          input()

        while opc_playa=="2":
          os.system("cls")



          playa_usar_intrf=(f"""                          {Fore.GREEN}#####
                        #######                                                                                                              
              ######    ########       #####                                                                                                                   {Fore.LIGHTWHITE_EX}Para usar un objeto casi siempre debe usarse{Fore.GREEN}
          ###########/#####\#####  #############                                                                                              
      ############/##########--#####################                                                                                                           {Fore.LIGHTWHITE_EX}con otro objeto u otro elmento del juego que pueda{Fore.GREEN}
    ####         ######################          #####                                                                                        
  ##          ####      ##########/@@              ###                                                                                                         {Fore.LIGHTWHITE_EX}aparecer en la narración o en las imágenes.{Fore.GREEN}
  #          ####        ,-.##/`.#\#####               ##
            ###        {Fore.YELLOW} /  |./  |,-. {Fore.GREEN}####                 #                                                                                                    {Fore.LIGHTWHITE_EX}Ahora, para usar dos objetos haz lo siguiente:{Fore.GREEN}
          ##           {Fore.YELLOW}\_,'\_,'|  \  {Fore.GREEN}###
          #             {Fore.YELLOW}\_{Fore.LIGHTBLACK_EX}$$$$${Fore.YELLOW}`._/   {Fore.GREEN}##                                                                                                                       {Fore.LIGHTWHITE_EX}(Escribe el nombre de un objeto, con, y el nombre del
                          {Fore.LIGHTBLACK_EX}$$$$${Fore.YELLOW}_/     {Fore.GREEN}# {Fore.LIGHTBLACK_EX}    
                          $$$$$                                                                                                                                {Fore.LIGHTWHITE_EX}otro objeto){Fore.LIGHTBLACK_EX}
                          $$$$$
                          $$$$$                                                                                                                                {Fore.LIGHTWHITE_EX}Por lo tanto, sería: {Fore.RED}"objeto" + "con" + "objeto"{Fore.LIGHTBLACK_EX}
                          $$$$$
                         $$$$$                                                                                                                                 {Fore.LIGHTWHITE_EX}El resultado sería: {Fore.RED}palo con cerillas{Fore.LIGHTBLACK_EX}
                        $$$$$
                        $$$$$                                                                                                                                  {Fore.RED}Importante: {Fore.LIGHTWHITE_EX}Los objetos siempre tienen que ir en el{Fore.LIGHTBLACK_EX}
                        $$$$$
                        $$$$$        ___                                                                                                                       {Fore.LIGHTWHITE_EX}orden en el que se muestran por pantalla, y deben ser{Fore.LIGHTBLACK_EX}
                        $$$$$    _.-'   `-._
                        $$$$$   ,'           `.                                                                                                                {Fore.LIGHTWHITE_EX}escritos igual{Fore.LIGHTBLACK_EX}
                        $$$$$  /               '
~~~~~~~~~~~~~~~~~~~~~~~$$$$$~~~'~~~~~~~~~~~~~~~~`~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~{Back.BLACK}                                                                     
{Back.BLUE}   ~      ~  ~    ~  ~ {Back.BLACK}{Fore.LIGHTBLACK_EX}$$$$${Back.BLUE}  ~   ~       ~          ~                                                                                {Back.BLACK}                                                                               
{Back.BLUE}       ~               {Back.BLACK}{Fore.LIGHTBLACK_EX}$$$$${Back.BLUE}     ~    ~          ~                                                                                    {Back.BLACK}                                                                
{Back.BLUE}  ~            ~    ~  {Back.BLACK}{Fore.LIGHTBLACK_EX}$$$$${Back.BLUE}~                     ~        ~                                                                          {Back.BLACK}                                                               
{Back.BLUE}                       {Back.BLACK}{Fore.LIGHTBLACK_EX}$$$$${Back.BLUE}                                                                                                          {Back.BLACK}                                                                                  
{Back.LIGHTYELLOW_EX}                       {Back.BLACK}{Fore.LIGHTBLACK_EX}$$$$${Back.LIGHTYELLOW_EX}                                                                                                          {Back.BLACK}                                                                                       
{Back.LIGHTYELLOW_EX}                       {Back.BLACK}{Fore.LIGHTBLACK_EX}$$$$${Back.LIGHTYELLOW_EX}                                                                                                          {Back.BLACK}                                                                                          
{Back.LIGHTYELLOW_EX}                       {Back.BLACK}{Fore.LIGHTBLACK_EX}$$$$${Back.LIGHTYELLOW_EX}    {Fore.BLACK}_      .                                                                                              {Back.BLACK}                                                                                       
{Back.LIGHTYELLOW_EX}                       {Back.BLACK}{Fore.LIGHTBLACK_EX}$$$$${Back.LIGHTYELLOW_EX}    {Fore.BLACK}\`-- -´|                                                                                              {Back.BLACK}                                                                                         
{Back.LIGHTYELLOW_EX}                      {Back.BLACK}{Fore.LIGHTBLACK_EX}$$$$$$${Back.LIGHTYELLOW_EX}    {Fore.BLACK}`----'                                                                                               {Back.BLACK}                                                                                         
{Back.LIGHTYELLOW_EX}                      {Back.BLACK}{Fore.LIGHTBLACK_EX}$$$$$$${Back.LIGHTYELLOW_EX}    {Fore.BLACK}banana                                                                                               {Back.BLACK}                                                                                         
{Back.LIGHTYELLOW_EX}                     {Back.BLACK}{Fore.LIGHTBLACK_EX}$$$$$$$$${Back.LIGHTYELLOW_EX}                                                                                                        {Back.BLACK}                                                                                          
{Back.LIGHTYELLOW_EX}                     {Back.BLACK}{Fore.LIGHTBLACK_EX}$$$$$$$$${Back.BLACK}
      """)


          print(playa_usar_intrf)      
          print(usar_intf)

          for i in list(objetos):
              contador_objetos+=1
              print(contador_objetos, objetos[contador_objetos-1])
          contador_objetos=0

          opc_usar=input("\n\n   --> ").lower()
          opc_playa=3



          while opc_playa==3:
                  
            if opc_usar=="palo con cerillas":

              print(" ¡Enhorabuena, has conseguido crear una antorcha, \n Este es tu inventario actualizado\n")

              objetos.remove(". Palo")
              objetos.remove(". Cerillas")
              objetos.append(". Antorcha")
                    
              for i in list(objetos):
                  contador_objetos+=1
                  print(contador_objetos, objetos[contador_objetos-1])
              contador_objetos=0

              print("\n Sigamos con la siguiente instrucción, pulsa m, para mostrar el menú.")  

              opc_playa=2

            else:
              print(Fore.LIGHTWHITE_EX, "Esta opción no está contemplada")
              input()
              os.system("cls")
              print(playa_usar_intrf)
              print(usar_intf)

              for i in list(objetos):
                  contador_objetos+=1
                  print(contador_objetos, objetos[contador_objetos-1])
              contador_objetos=0

              opc_usar=input("\n\n   --> ").lower()


          opc_menu=input("     --> ")
          while  opc_menu!="m":
              print(Fore.LIGHTWHITE_EX, "Esta opción no está contemplada")
              input()
              os.system("cls")
              print(playa_usar_intrf)
              print(usar_intf)
              print("\n Sigamos con la siguiente instrucción, pulsa m, para mostrar el menú.")
              opc_menu=input("     --> ")







          while opc_menu=="m":
            os.system("cls")


            print(f"""                        {Fore.GREEN}#####
                        #######                                                                                                              
              ######    ########       #####                                                                                                                        {Fore.LIGHTWHITE_EX}De acuerdo, la tercera acción es la de {Fore.RED}"coger".{Fore.GREEN} 
          ###########/#####\#####  #############                                                                                              
      ############/##########--#####################                                                                                                                {Fore.LIGHTWHITE_EX}Esta acción consiste en coger un objeto{Fore.GREEN} 
    ####         ######################          #####                                                                                                              
  ##          ####      ##########/@@              ###                                                                                                              {Fore.LIGHTWHITE_EX}Para ello, pulsamos {Fore.RED}1{Fore.LIGHTWHITE_EX}, y cuando se{Fore.GREEN}   
  #          ####        ,-.##/`.#\#####               ##                                                                                                            
            ###        {Fore.YELLOW} /  |./  |,-. {Fore.GREEN}####                 #                                                                                                         {Fore.LIGHTWHITE_EX}abra la opción de coger, {Fore.RED}escribiremos{Fore.GREEN}
          ##           {Fore.YELLOW}\_,'\_,'|  \  {Fore.GREEN}###                                                                                                   
          #             {Fore.YELLOW}\_{Fore.LIGHTBLACK_EX}$$$$${Fore.YELLOW}`._/   {Fore.GREEN}##                                                                                                                            {Fore.RED}el objeto que queremos coger{Fore.LIGHTWHITE_EX}, este objeto{Fore.GREEN}
                          {Fore.LIGHTBLACK_EX}$$$$${Fore.YELLOW}_/     {Fore.GREEN}#{Fore.LIGHTBLACK_EX}                                                                                                                           
                         $$$$$                                                                                                                                      {Fore.LIGHTWHITE_EX}se guardará en el inventario.{Fore.LIGHTBLACK_EX}  
                        $$$$$                                                                                                                                    
                        $$$$$                                                                                                                                   
                        $$$$$                                                                                                                                      
                        $$$$$                                                                                                                                     
                        $$$$$                                                                                                                                      
                        $$$$$                                                                                                                                     
                        $$$$$                                                                                                                                       
                        $$$$$        ___
                        $$$$$    _.-'   `-._                                                                                                                       
                        $$$$$   ,'           `.
                        $$$$$  /               '                                                                                                                   
~~~~~~~~~~~~~~~~~~~~~~~$$$$$~~~'~~~~~~~~~~~~~~~~`~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~{Back.BLACK}                                                                     
{Back.BLUE}   ~      ~  ~    ~  ~ {Back.BLACK}{Fore.LIGHTBLACK_EX}$$$$${Back.BLUE}  ~   ~       ~          ~                                                                                {Back.BLACK}                                                                               
{Back.BLUE}       ~               {Back.BLACK}{Fore.LIGHTBLACK_EX}$$$$${Back.BLUE}     ~    ~          ~                                                                                    {Back.BLACK}                                              
{Back.BLUE}  ~            ~    ~  {Back.BLACK}{Fore.LIGHTBLACK_EX}$$$$${Back.BLUE}~                     ~        ~                                                                          {Back.BLACK}                                                                            
{Back.BLUE}                       {Back.BLACK}{Fore.LIGHTBLACK_EX}$$$$${Back.BLUE}                                                                                                          {Back.BLACK}                                                          
{Back.LIGHTYELLOW_EX}                       {Back.BLACK}{Fore.LIGHTBLACK_EX}$$$$${Back.LIGHTYELLOW_EX}                                                                                                          {Back.BLACK}                                                               
{Back.LIGHTYELLOW_EX}                       {Back.BLACK}{Fore.LIGHTBLACK_EX}$$$$${Back.LIGHTYELLOW_EX}                                                                                                          {Back.BLACK}                                                     
{Back.LIGHTYELLOW_EX}                       {Back.BLACK}{Fore.LIGHTBLACK_EX}$$$$${Back.LIGHTYELLOW_EX}    {Fore.BLACK}_      .                                                                                              {Back.BLACK}                                                                   
{Back.LIGHTYELLOW_EX}                       {Back.BLACK}{Fore.LIGHTBLACK_EX}$$$$${Back.LIGHTYELLOW_EX}    {Fore.BLACK}\`-- -´|                                                                                              {Back.BLACK}                                                                
{Back.LIGHTYELLOW_EX}                      {Back.BLACK}{Fore.LIGHTBLACK_EX}$$$$$$${Back.LIGHTYELLOW_EX}    {Fore.BLACK}`----'                                                                                               {Back.BLACK}                                                                        
{Back.LIGHTYELLOW_EX}                      {Back.BLACK}{Fore.LIGHTBLACK_EX}$$$$$$${Back.LIGHTYELLOW_EX}    {Fore.BLACK}banana                                                                                               {Back.BLACK}                                                             
{Back.LIGHTYELLOW_EX}                     {Back.BLACK}{Fore.LIGHTBLACK_EX}$$$$$$$$${Back.LIGHTYELLOW_EX}                                                                                                        {Back.BLACK}                                                      
{Back.LIGHTYELLOW_EX}                     {Back.BLACK}{Fore.LIGHTBLACK_EX}$$$$$$$$${Back.BLACK}
                """)
                
            print(acciones)
            opc_playa=input("\n\n   --> ").lower()

            if opc_playa!="1":
              print(Fore.LIGHTWHITE_EX, "Esta opción no está contemplada")
              input()

            while opc_playa=="1":
              os.system("cls")



              playa_coger_intrf=(f"""                       {Fore.GREEN}#####
                        #######                                                                                                              
              ######    ########       #####                                                                                                                   {Fore.LIGHTWHITE_EX}Los objetos que podremos coger se{Fore.GREEN}
          ###########/#####\#####  #############                                                                                              
      ############/##########--#####################                                                                                                           {Fore.LIGHTWHITE_EX}presentan en los dibujos o en el{Fore.GREEN}
    ####         ######################          #####                                                                                        
  ##          ####      ##########/@@              ###                                                                                                         {Fore.LIGHTWHITE_EX}texto narrativo, por lo que debemos{Fore.GREEN}
  #          ####        ,-.##/`.#\#####               ##
            ###        {Fore.YELLOW} /  |./  |,-. {Fore.GREEN}####                 #                                                                                                    {Fore.LIGHTWHITE_EX}estar muy atentos.{Fore.GREEN}
          ##           {Fore.YELLOW}\_,'\_,'|  \  {Fore.GREEN}###
          #             {Fore.YELLOW}\_{Fore.LIGHTBLACK_EX}$$$$${Fore.YELLOW}`._/   {Fore.GREEN}##                                                                                                                       {Fore.LIGHTWHITE_EX}Vamos a hacer una prueba para ver si lo
                          {Fore.LIGHTBLACK_EX}$$$$${Fore.YELLOW}_/     {Fore.GREEN}#{Fore.LIGHTBLACK_EX}    
                          $$$$$                                                                                                                                {Fore.LIGHTWHITE_EX}hemos entendido, coge la {Fore.RED}banana {Fore.LIGHTWHITE_EX}de la orilla{Fore.LIGHTBLACK_EX}
                          $$$$$
                         $$$$$                                                                                                                               
                        $$$$$
                        $$$$$                                                                                                                                
                        $$$$$
                        $$$$$                                                                                                                                 
                        $$$$$
                        $$$$$        ___                                                                                                                      
                        $$$$$    _.-'   `-._
                        $$$$$   ,'           `.                                                                                                               
                        $$$$$  /               '
~~~~~~~~~~~~~~~~~~~~~~~$$$$$~~~'~~~~~~~~~~~~~~~~`~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~{Back.BLACK}                                                                     
{Back.BLUE}   ~      ~  ~    ~  ~ {Back.BLACK}{Fore.LIGHTBLACK_EX}$$$$${Back.BLUE}  ~   ~       ~          ~                                                                                {Back.BLACK}                                                                               
{Back.BLUE}       ~               {Back.BLACK}{Fore.LIGHTBLACK_EX}$$$$${Back.BLUE}     ~    ~          ~                                                                                    {Back.BLACK}                                                                
{Back.BLUE}  ~            ~    ~  {Back.BLACK}{Fore.LIGHTBLACK_EX}$$$$${Back.BLUE}~                     ~        ~                                                                          {Back.BLACK}                                                               
{Back.BLUE}                       {Back.BLACK}{Fore.LIGHTBLACK_EX}$$$$${Back.BLUE}                                                                                                          {Back.BLACK}                                                                                  
{Back.LIGHTYELLOW_EX}                       {Back.BLACK}{Fore.LIGHTBLACK_EX}$$$$${Back.LIGHTYELLOW_EX}                                                                                                          {Back.BLACK}                                                                                       
{Back.LIGHTYELLOW_EX}                       {Back.BLACK}{Fore.LIGHTBLACK_EX}$$$$${Back.LIGHTYELLOW_EX}                                                                                                          {Back.BLACK}                                                                                          
{Back.LIGHTYELLOW_EX}                       {Back.BLACK}{Fore.LIGHTBLACK_EX}$$$$${Back.LIGHTYELLOW_EX}    {Fore.BLACK}_      .                                                                                              {Back.BLACK}                                                                                       
{Back.LIGHTYELLOW_EX}                       {Back.BLACK}{Fore.LIGHTBLACK_EX}$$$$${Back.LIGHTYELLOW_EX}    {Fore.BLACK}\`-- -´|                                                                                              {Back.BLACK}                                                                                         
{Back.LIGHTYELLOW_EX}                      {Back.BLACK}{Fore.LIGHTBLACK_EX}$$$$$$${Back.LIGHTYELLOW_EX}    {Fore.BLACK}`----'                                                                                               {Back.BLACK}                                                                                         
{Back.LIGHTYELLOW_EX}                      {Back.BLACK}{Fore.LIGHTBLACK_EX}$$$$$$${Back.LIGHTYELLOW_EX}    {Fore.BLACK}banana                                                                                               {Back.BLACK}                                                                                         
{Back.LIGHTYELLOW_EX}                     {Back.BLACK}{Fore.LIGHTBLACK_EX}$$$$$$$$${Back.LIGHTYELLOW_EX}                                                                                                        {Back.BLACK}                                                                                          
{Back.LIGHTYELLOW_EX}                     {Back.BLACK}{Fore.LIGHTBLACK_EX}$$$$$$$$${Back.BLACK}
              """)
                        
              print(playa_coger_intrf)
              print(coger_intf)

              palabra_coger=input("\n\n   --> ").lower()
              opc_playa=3

              while opc_playa==3:
                          
                if palabra_coger=="banana":

                  os.system("cls")
                  print(playa)
                  print(coger_intf)

                  print(" ¡Enhorabuena, has cogido un platano, \n Este es tu inventario actualizado\n")

                  objetos.append(". Banana")

                            
                  for i in list(objetos):
                      contador_objetos+=1
                      print(contador_objetos, objetos[contador_objetos-1])
                  contador_objetos=0

                  opc_playa=2

                else:
                  print(Fore.LIGHTWHITE_EX, "Esta opción no está contemplada")
                  input()
                  os.system("cls")
                  print(playa_coger_intrf)
                  print(coger_intf)
                  palabra_coger=input("\n\n   --> ").lower()





              opc_menu=input("\nPulsa cualquier tecla para continuar     --> ")
              os.system("cls")



              print(f"""
                          {Fore.GREEN}#####
                       #######                                                                                                              
            ######    ########       #####                                                                                                                  {Fore.LIGHTWHITE_EX}De acuerdo, la tercera acción es la de {Fore.RED}"dar"{Fore.GREEN}
        ###########/#####\#####  #############                                                                                              
    ############/##########--#####################                                                                                                          {Fore.LIGHTWHITE_EX}Esta acción consiste en dar un objeto a algo{Fore.GREEN}  
  ####         ######################          #####                                                                                        
 ##          ####      ##########/@@              ###                                                                                                       {Fore.LIGHTWHITE_EX}o a alguien, su sintaxis para ejecutarla{Fore.GREEN}   
#          ####        ,-.##/`.#\#####               ##
          ###        {Fore.YELLOW} /  |./  |,-. {Fore.GREEN}####                 #                                                                                                   {Fore.RED}"a" en vez de "con", por ejemplo:{Fore.GREEN}
         ##           {Fore.YELLOW}\_,'\_,'|  \  {Fore.GREEN}###
         #             {Fore.YELLOW}\_{Fore.LIGHTBLACK_EX}$$$$${Fore.YELLOW}`._/   {Fore.GREEN}##                                                                                                                     {Fore.LIGHTWHITE_EX}Pulsamos: {Fore.RED}3{Fore.LIGHTBLACK_EX}
                          {Fore.LIGHTBLACK_EX}$$$$${Fore.YELLOW}_/     {Fore.GREEN}# {Fore.LIGHTBLACK_EX}    
                          $$$$$                                                                                                                             {Fore.LIGHTWHITE_EX}Escribimos: {Fore.RED}Antorcha a Pirata{Fore.LIGHTBLACK_EX} 
                          $$$$$
                          $$$$$                                                                                                                             {Fore.LIGHTWHITE_EX}¡Genial!, una vez que ya sabemos como jugar{Fore.LIGHTBLACK_EX}
                          $$$$$
                          $$$$$                                                                                                                             {Fore.LIGHTWHITE_EX}vamos a empezar con nuestra aventura,{Fore.LIGHTBLACK_EX}
                         $$$$$
                         $$$$$                                                                                                                              {Fore.LIGHTWHITE_EX}para ello, pulsa cualquier tecla.{Fore.LIGHTBLACK_EX}
                         $$$$$
                         $$$$$        ___
                         $$$$$    _.-'   `-._
                        $$$$$   ,'           `.
                        $$$$$  /               '
~~~~~~~~~~~~~~~~~~~~~~~$$$$$~~~'~~~~~~~~~~~~~~~~`~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~{Back.BLACK}                                                                     
{Back.BLUE}   ~      ~  ~    ~  ~ {Back.BLACK}{Fore.LIGHTBLACK_EX}$$$$${Back.BLUE}  ~   ~       ~          ~                                                                                {Back.BLACK}                                                                               
{Back.BLUE}       ~               {Back.BLACK}{Fore.LIGHTBLACK_EX}$$$$${Back.BLUE}     ~    ~          ~                                                                                    {Back.BLACK}                                                                                           
{Back.BLUE}  ~            ~    ~  {Back.BLACK}{Fore.LIGHTBLACK_EX}$$$$${Back.BLUE}~                     ~        ~                                                                          {Back.BLACK}                    
{Back.BLUE}                       {Back.BLACK}{Fore.LIGHTBLACK_EX}$$$$${Back.BLUE}                                                                                                          {Back.BLACK}
{Back.LIGHTYELLOW_EX}                       {Back.BLACK}{Fore.LIGHTBLACK_EX}$$$$${Back.LIGHTYELLOW_EX}                                                                                                          {Back.BLACK}
{Back.LIGHTYELLOW_EX}                       {Back.BLACK}{Fore.LIGHTBLACK_EX}$$$$${Back.LIGHTYELLOW_EX}                                                                                                          {Back.BLACK}                                                                                        
{Back.LIGHTYELLOW_EX}                       {Back.BLACK}{Fore.LIGHTBLACK_EX}$$$$${Back.LIGHTYELLOW_EX}                                                                                                          {Back.BLACK}                                                                                             
{Back.LIGHTYELLOW_EX}                       {Back.BLACK}{Fore.LIGHTBLACK_EX}$$$$${Back.LIGHTYELLOW_EX}                                                                                                          {Back.BLACK}                                                                                       
{Back.LIGHTYELLOW_EX}                      {Back.BLACK}{Fore.LIGHTBLACK_EX}$$$$$$${Back.LIGHTYELLOW_EX}                                                                                                         {Back.BLACK}                                                                                            
{Back.LIGHTYELLOW_EX}                      {Back.BLACK}{Fore.LIGHTBLACK_EX}$$$$$$${Back.LIGHTYELLOW_EX}                                                                                                         {Back.BLACK}                                                                                             
{Back.LIGHTYELLOW_EX}                     {Back.BLACK}{Fore.LIGHTBLACK_EX}$$$$$$$$${Back.LIGHTYELLOW_EX}                                                                                                        {Back.BLACK}                                                                                             
{Back.LIGHTYELLOW_EX}                     {Back.BLACK}{Fore.LIGHTBLACK_EX}$$$$$$$$${Back.BLACK}
""")



              opc_playa=input()
              os.system("cls")
              playa_v=False
              opc_playa=False
              opc_menu=False




  
pygame.mixer.music.stop()


#Desde la playa hasta la tribu

mapa_anim=mapa.replace(f"{a}", f"{personaje_unicode}", 7)
come_back=mapa_anim.replace(f"{personaje_unicode}", f"{a}", 6)
print(come_back)
time.sleep(1)
os.system("cls")


mapa_anim=mapa.replace(f"{c}", f"{personaje_unicode}", 2)
come_back=mapa_anim.replace(f"{personaje_unicode}", f"{c}", 1)
print(come_back)
time.sleep(1)
os.system("cls")


mapa_anim=mapa.replace(f"{a}", f"{personaje_unicode}", 6)
come_back=mapa_anim.replace(f"{personaje_unicode}", f"{a}", 5)
print(come_back)
time.sleep(1)
os.system("cls")


pygame.mixer.music.load(song_tribu)
pygame.mixer.music.play(-1)


for i in range(4):
    print(tribu)
    time.sleep(1)
    os.system("cls")

    print(tribu_anim)
    time.sleep(1)
    os.system("cls")

for _ in texto_tribu:
    print(_, end="", flush=True)
    
    if _!="\t":
        time.sleep(0.04)


input(f"\n\n\t\t\t\t\t\t\t\t\t\t\t{Fore.LIGHTWHITE_EX}Pulsa cualquier tecla para continuar: ")

os.system("cls")

print(f"""{Fore.RED}
:-..                        .:. .                         . :-                         .....        
.                          ....                         .: .                         ...:.          
    .              #*-.=@=.-=#%%@@@@@@@@@@@@@@@@@@@@@.  -..   ..                     ...    .       
      .         .+%.                               %@@.         .                 .          .     
       ..     @         {Fore.LIGHTWHITE_EX}¡Hola, forastero!, no sé{Fore.RED}     @@.         .              .              .   
          .   @   {Fore.LIGHTWHITE_EX}cómo has acabado aquí, hace tiempo{Fore.RED}   @@+         .          .                  . 
           .  @  {Fore.LIGHTWHITE_EX}que no veo a un 'sinverguenza' cómo tú.{Fore.RED} @*          .       .                     
             .@@    {Fore.LIGHTWHITE_EX}El último que vino se ganó nuestra{Fore.RED}    @%                .                       
             ++:   {Fore.LIGHTWHITE_EX}confianza, pero no sabemos si podemos{Fore.RED}  @#             ...                        
             **   {Fore.LIGHTWHITE_EX}confiar en ti o no.{Fore.RED}                     @=                                        
           . %*   {Fore.LIGHTWHITE_EX}LLevamos tiempo sin encontrar animales,{Fore.RED} @@-          .       .                    .
          .  %=   {Fore.LIGHTWHITE_EX}tenemos hambre, y el tiempo pone cada{Fore.RED}    @         .          .                  . 
       ..    %+ {Fore.LIGHTWHITE_EX}cosa en su sitio, en este caso a tí, para{Fore.RED}  @=                     .              .   
      .      -@  {Fore.LIGHTWHITE_EX}que nos sirvas de alimento, a no ser que{Fore.RED} -@      .                 .          .     
  ...        .@@    {Fore.LIGHTWHITE_EX}demuestres lo contrario.{Fore.RED}           @@@@ ....                     .    .-.       
 ....           .@                                    @:    .....                         :-:-       
...               @=                                @.    . .                          -...         
..                .@@@@@@@%+=-......@@@@@@@@@@@@@@@@@   ....                         --:-.          
    .                      -:.@.....@:                  ..     .  @.                  ..    .       
      .                 .     .@....**                           .=@               :          .     
        .              .       .%@...@             ..  ..         .@@=.          .              .   
          .         .             @%.#+.         =@@%....@@+      :@::%@@      .                  : 
           ..      .               .@@@. .     :%:..........%@.   %%:@:@*..@@*.                    .
                                      @@.     @@..............@%   .@@@@::@-@ .                     
              -..                       .  ..+@................+@   .@%*@==-@@.                     
             .                            . .@*.................@=   *@*@.  .                       
           .       .                        -@...................@    @@=@   ..                    .
         .           :          %@@@@@.     *%..#.@..............@  .  @=%+     .                   
       ..             ..        @@..@@:   .@.@................:.@@:     @-@      .              .   
                         .    .@*...#@@.     @@@@+.   :*@@.....#-@-     .@-+@.@-   .                
  -:.                     .    ..:@.@@                  .#@..--..@:     %#.@@@.@.    .    ...       
:-:-.                        ....:@.=@      *@@@@@@@.@@#..@-.-...@.     .@.#@=.@.       .....       
...                         ....  @..@     .@*=::........:-:.....@    . @..@@=@=       ....         
-                         ....    :@.=@.    %@..........-:......*@.   .@:.@.@*=@.   .....           
    .                      ..     .:@.+@    .@-......:--+#%@@#++@@   *@.+@. .@-+@.    ..            
      ..                :          ..@@.@@.  @@#+:%#%@++@*=:....@+ .@#.@*    .@-#@.           ..    
        .             .                %@+=@@@....*@.+..@.......:@@:.@@.      -@-@:             .   
          .         .                  . .@@=.....@@..@@@+........#@%.         +@-@.              . 
            .     .                      .  @-.......%@*=-:......@.    .     .  #@-@.               
                                            %+.......%:+%........@               %@-@               
              ..                           .+@........@:%.......:@       ...      @@-@.             
             .                              .@..........-.......*@.     .   .      @@#*             
           :       .                    .    .@@*@%@@==@@%@@+++++%@  .        .                    .
         .           .                ..     *@++++++++#+@++++#+++@@.           :                .  
       .               .            .        .@+++++++++++++++=*++=@%             .            .    
                         .         .          @+++++%+++++++%+++++@#@              .                
  ....                         :-:.          .@+++++++++++++++==+@                        :.-.      
...:.                        ....-           .@@@++*+++@@%@@#.#-@@                      -....       
...                        .---:               @.+@ .@@. ..*. -@.*.                   :.-.:         
.                         .. .                .@.@@  ::.....   @...+@               ....-           
    ..                   . ..     .           .@..@    . .     .@@#.                  ..    ..      
       .               ..           :        .@...@  .           .                .            .    
        .             .              .        .  . .               .             .              .   
          .         .                   .        .                   .        ..                  . 

""")

input(f"{Fore.LIGHTWHITE_EX}Pulsa cualquier tecla para continuar: ")

os.system("cls")

print(f"""{Fore.RED}
:-..                        .:. .                         . :-                         .....        
.                          ....                         .: .                         ...:.          
    .              #*-.=@=.-=#%%@@@@@@@@@@@@@@@@@@@@@.  -..   ..                     ...    .       
      .         .+%.                               %@@.         .                 .          .     
       ..     @         {Fore.LIGHTWHITE_EX}No sé si te has dado cuenta,{Fore.RED}  @@.         .              .              .   
          .   @    {Fore.LIGHTWHITE_EX}pero somos adoradores del tiempo,{Fore.RED}    @@+         .          .                  . 
           .  @   {Fore.LIGHTWHITE_EX}y es en lo único en lo que creemos.{Fore.RED}     @*          .       .                     
             .@@      {Fore.LIGHTWHITE_EX}Piensa en algo, quizás puedas{Fore.RED}       @%                .                       
             ++:   {Fore.LIGHTWHITE_EX}demostrarnos tu confianza, de alguna{Fore.RED}   @#             ...                        
             **   {Fore.LIGHTWHITE_EX}manera, al igual que hizo el anterior{Fore.RED}   @=                                        
           . %*   {Fore.LIGHTWHITE_EX}forastero.{Fore.RED}                              @@-          .       .                    .
          .  %=                                           @         .          .                  . 
       ..    %+                                           @=                     .              .   
      .      -@                                          -@      .                 .          .     
  ...        .@@                                       @@@@ ....                     .    .-.       
 ....           .@                                    @:    .....                         :-:-       
...               @=                                @.    . .                          -...         
..                .@@@@@@@%+=-......@@@@@@@@@@@@@@@@@   ....                         --:-.          
    .                      -:.@.....@:                  ..     .  @.                  ..    .       
      .                 .     .@....**                           .=@               :          .     
        .              .       .%@...@             ..  ..         .@@=.          .              .   
          .         .             @%.#+.         =@@%....@@+      :@::%@@      .                  : 
           ..      .               .@@@. .     :%:..........%@.   %%:@:@*..@@*.                    .
                                      @@.     @@..............@%   .@@@@::@-@ .                     
              -..                       .  ..+@................+@   .@%*@==-@@.                     
             .                            . .@*.................@=   *@*@.  .                       
           .       .                        -@...................@    @@=@   ..                    .
         .           :          %@@@@@.     *%..#.@..............@  .  @=%+     .                   
       ..             ..        @@..@@:   .@.@................:.@@:     @-@      .              .   
                         .    .@*...#@@.     @@@@+.   :*@@.....#-@-     .@-+@.@-   .                
  -:.                     .    ..:@.@@                  .#@..--..@:     %#.@@@.@.    .    ...       
:-:-.                        ....:@.=@      *@@@@@@@.@@#..@-.-...@.     .@.#@=.@.       .....       
...                         ....  @..@     .@*=::........:-:.....@    . @..@@=@=       ....         
-                         ....    :@.=@.    %@..........-:......*@.   .@:.@.@*=@.   .....           
    .                      ..     .:@.+@    .@-......:--+#%@@#++@@   *@.+@. .@-+@.    ..            
      ..                :          ..@@.@@.  @@#+:%#%@++@*=:....@+ .@#.@*    .@-#@.           ..    
        .             .                %@+=@@@....*@.+..@.......:@@:.@@.      -@-@:             .   
          .         .                  . .@@=.....@@..@@@+........#@%.         +@-@.              . 
            .     .                      .  @-.......%@*=-:......@.    .     .  #@-@.               
                                            %+.......%:+%........@               %@-@               
              ..                           .+@........@:%.......:@       ...      @@-@.             
             .                              .@..........-.......*@.     .   .      @@#*             
           :       .                    .    .@@*@%@@==@@%@@+++++%@  .        .                    .
         .           .                ..     *@++++++++#+@++++#+++@@.           :                .  
       .               .            .        .@+++++++++++++++=*++=@%             .            .    
                         .         .          @+++++%+++++++%+++++@#@              .                
  ....                         :-:.          .@+++++++++++++++==+@                        :.-.      
...:.                        ....-           .@@@++*+++@@%@@#.#-@@                      -....       
...                        .---:               @.+@ .@@. ..*. -@.*.                   :.-.:         
.                         .. .                .@.@@  ::.....   @...+@               ....-           
    ..                   . ..     .           .@..@    . .     .@@#.                  ..    ..      
       .               ..           :        .@...@  .           .                .            .    
        .             .              .        .  . .               .             .              .   
          .         .                   .        .                   .        ..                  . 

""")





while juego_v==True:

    while tribu_v==True:    

        opc_menu=input(f"{Fore.LIGHTWHITE_EX}Pulsa 'm' y Enter para abrir el menú: ")

        if opc_menu=="m":

          os.system("cls")

          print(tribu_menu)
          print(acciones)
            
          print("|  Indica la acción que quieres realizar: ")
          opcion_acc=input("|       --> ")
        

          match opcion_acc:
              case "1":
                      
                  os.system("cls")

                  print(tribu_menu)
                  print(coger_intf)
                  opcion_coger=input("       --> ")
                  print("Ahora mismo no hay nada que coger")
                  input("Pulsa Enter para continuar")


              case "2":
                  os.system("cls")
                  print(tribu_menu)
                  print(usar_intf)

                  for i in list(objetos):
                      contador_objetos+=1
                      print(contador_objetos, objetos[contador_objetos-1])
                  contador_objetos=0

                  opcion_usar=input("       --> ")
                  print("Esos objetos no se pueden usar")
                  input("Pulsa Enter para continuar")


              case "3":
                  os.system("cls")
                  print(tribu_menu)
                  print(dar_intf)

                  for i in list(objetos):
                      contador_objetos+=1
                      print(contador_objetos, objetos[contador_objetos-1])
                  contador_objetos=0

                  opcion_dar=input("       --> ").lower()

                  if opcion_dar=="reloj" or opcion_dar=="reloj a jefe":
                      print("¡Genial!, le has dado el reloj al jefe de la tribu")
                      objetos.remove(". Reloj")
                      input("Pulsa Enter para continuar")
                      os.system("cls")
                      opcion_menu=False
                      tribu_v=False

                  else:
                      print("No puedes dar este objeto")
                      input("Pulsa Enter para continuar")


              case "4":
                  os.system("cls")
                  print(tribu_menu)
                  print(inventario_intf)

                  for i in list(objetos):
                      contador_objetos+=1
                      print(contador_objetos, objetos[contador_objetos-1])
                  contador_objetos=0

                  input("\nPulsa Enter para continuar")

              case _:
                print("Lo siento, está opción no está contemplada")    

        else:
            print("Lo siento, está opción no está contemplada")    

              

                    






    print(f"""{Fore.RED}
:-..                        .:. .                         . :-                         .....        
.                          ....                         .: .                         ...:.          
    .              #*-.=@=.-=#%%@@@@@@@@@@@@@@@@@@@@@.  -..   ..                     ...    .       
      .         .+%.                               %@@.         .                 .          .     
       ..     @         {Fore.LIGHTWHITE_EX}¡Caray! un instrumento{Fore.RED}        @@.         .              .              .   
          .   @    {Fore.LIGHTWHITE_EX}para medir el tiempo, nuestro{Fore.RED}        @@+         .          .                  . 
           .  @   {Fore.LIGHTWHITE_EX}dios, estará muy agradecido y esto{Fore.RED}      @*          .       .                     
             .@@      {Fore.LIGHTWHITE_EX}nos honra, dejaremos que sigas{Fore.RED}      @%                .                       
             ++:   {Fore.LIGHTWHITE_EX}con tu camino.{Fore.RED}                         @#             ...                        
             **   {Fore.LIGHTWHITE_EX}Además, para mostrarte nuestro{Fore.RED}          @=                                        
           . %*   {Fore.LIGHTWHITE_EX}agradecimiento, queremos obsequiarte{Fore.RED}    @@-          .       .                    .
          .  %=   {Fore.LIGHTWHITE_EX}con un pollo de nuestro ganado.{Fore.RED}         @         .          .                  . 
       ..    %+   {Fore.LIGHTWHITE_EX}Si quieres un consejo, ten cuidado{Fore.RED}      @=                     .              .   
      .      -@   {Fore.LIGHTWHITE_EX}con la bestia que surca las aguas{Fore.RED}      -@      .                 .          .     
  ...        .@@    {Fore.LIGHTWHITE_EX}del interior, ya acabó con el{Fore.RED}      @@@@ ....                     .    .-.       
 ....           .@    {Fore.LIGHTWHITE_EX}otro forastero y no queremos{Fore.RED}    @:    .....                         :-:-       
...               @=   {Fore.LIGHTWHITE_EX}que la historia se repita{Fore.RED}    @.    . .                          -...         
..                .@@@@@@@%+=-......@@@@@@@@@@@@@@@@@   ....                         --:-.          
    .                      -:.@.....@:                  ..     .  @.                  ..    .       
      .                 .     .@....**                           .=@               :          .     
        .              .       .%@...@             ..  ..         .@@=.          .              .   
          .         .             @%.#+.         =@@%....@@+      :@::%@@      .                  : 
           ..      .               .@@@. .     :%:..........%@.   %%:@:@*..@@*.                    .
                                      @@.     @@..............@%   .@@@@::@-@ .                     
              -..                       .  ..+@................+@   .@%*@==-@@.                     
             .                            . .@*.................@=   *@*@.  .                       
           .       .                        -@...................@    @@=@   ..                    .
         .           :          %@@@@@.     *%..#.@..............@  .  @=%+     .                   
       ..             ..        @@..@@:   .@.@................:.@@:     @-@      .              .   
                         .    .@*...#@@.     @@@@+.   :*@@.....#-@-     .@-+@.@-   .                
  -:.                     .    ..:@.@@                  .#@..--..@:     %#.@@@.@.    .    ...       
:-:-.                        ....:@.=@      *@@@@@@@.@@#..@-.-...@.     .@.#@=.@.       .....       
...                         ....  @..@     .@*=::........:-:.....@    . @..@@=@=       ....         
-                         ....    :@.=@.    %@..........-:......*@.   .@:.@.@*=@.   .....           
    .                      ..     .:@.+@    .@-......:--+#%@@#++@@   *@.+@. .@-+@.    ..            
      ..                :          ..@@.@@.  @@#+:%#%@++@*=:....@+ .@#.@*    .@-#@.           ..    
        .             .                %@+=@@@....*@.+..@.......:@@:.@@.      -@-@:             .   
          .         .                  . .@@=.....@@..@@@+........#@%.         +@-@.              . 
            .     .                      .  @-.......%@*=-:......@.    .     .  #@-@.               
                                            %+.......%:+%........@               %@-@               
              ..                           .+@........@:%.......:@       ...      @@-@.             
             .                              .@..........-.......*@.     .   .      @@#*             
           :       .                    .    .@@*@%@@==@@%@@+++++%@  .        .                    .
         .           .                ..     *@++++++++#+@++++#+++@@.           :                .  
       .               .            .        .@+++++++++++++++=*++=@%             .            .    
                         .         .          @+++++%+++++++%+++++@#@              .                
  ....                         :-:.          .@+++++++++++++++==+@                        :.-.      
...:.                        ....-           .@@@++*+++@@%@@#.#-@@                      -....       
...                        .---:               @.+@ .@@. ..*. -@.*.                   :.-.:         
.                         .. .                .@.@@  ::.....   @...+@               ....-           
    ..                   . ..     .           .@..@    . .     .@@#.                  ..    ..      
       .               ..           :        .@...@  .           .                .            .    
        .             .              .        .  . .               .             .              .   
          .         .                   .        .                   .        ..                  . 

""")



    input(f"{Fore.LIGHTWHITE_EX}Pulsa Enter para continuar: ")
    os.system("cls")


    texto2=f"""{Fore.LIGHTWHITE_EX}
    ¡Genial!, se te ha añadido un nuevo objeto en tu inventario.

    Este es tu inventario actualizado"""

    objetos.append(". Pollo")

    for _ in texto2:
        print(_, end="", flush=True)
        time.sleep(0.04)
    
    input("\n\nPulsa cualquier tecla para ver tu inventario actualizado: ")

    os.system("cls")

    print(inventario_intf)

    for i in list(objetos):
        contador_objetos+=1
        print(contador_objetos, objetos[contador_objetos-1])
    contador_objetos=0

    input("\nPulsa cualquier tecla para continuar con la historia: ")
    os.system("cls")


    pygame.mixer.music.stop()


#Desde la tribu hasta la selva

    mapa_anim=mapa.replace(f"{d}", f"{personaje_unicode}", 4)
    come_back=mapa_anim.replace(f"{personaje_unicode}", f"{d}", 3)
    print(come_back)
    time.sleep(1)
    os.system("cls")


    mapa_anim=mapa.replace(f"{a}", f"{personaje_unicode}", 5)
    come_back=mapa_anim.replace(f"{personaje_unicode}", f"{a}", 4)
    print(come_back)
    time.sleep(1)
    os.system("cls")


    mapa_anim=mapa.replace(f"{a}", f"{personaje_unicode}", 4)
    come_back=mapa_anim.replace(f"{personaje_unicode}", f"{a}", 3)
    print(come_back)
    time.sleep(1)
    os.system("cls")

                            
    pygame.mixer.music.load(song_selva)
    pygame.mixer.music.play(-1)



    print(f"""{Fore.LIGHTWHITE_EX}
    @@@@@@@@@@@@@@@@@@@%@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%@%:+%@@@@%%%#*%#%%*%#@*@@@@%%@@%@%%%@%@@@%%@@@@%%@@@@@@@@@@@@@@@@@@@@@@@@@@@
    @@@@@@@@@@@@@@@@@@@%@@@@@@@@@@@%%@@@@@@@@@@@@@@@@@@@@@@#%@@@%%%*=#%%#%%%%%%%@*@@@@@@@%*-%@@@@%@@@@@@@%#@@@%@@%%%%%@@@@@@@@@@@@@@@
    @@@@@@@@@@@@@@@@@@@@@@%%@@@@%@%@%%%@@@@@@@%%@%@@@@@@%%@#@@@@.*@#%%--:%#%%%#%@@@%%%%%%@@%@%@@@@@@@@@@@%@@@%@@@@%@@@@@@@@@@@@@@@@@@
    @@@@@@@@@@@@@@@@@@@@@@@@@%#%%%%%%%%%@%@%@@%@%%%@@@@@@%%%@@@:..*-%%#%%%@%%%%%%%%%%%%*%%%%%%@#%%%%%@@@@%%%%%@%@@@@@@@@@@@@@@%@@@@@@
    @@@@@@@@@@@@%@@@@@@@@@@@%%%%%%%%%###%%%@@@%%%%%%%%%@%%%%@@@:..++%%%%%%@%%%%%%%%%%%%%%@%%%%%%+*%%%@@@@#%%%@@@@@@%%@@@%@@@@@@%@@@@@
    @@@@@@@@@@@@@%@@@@%%%@%%@%%%%%%%###+*%@@%%###%%%%%%%%%%%@@@%%#%%%%%%%%%%%%%%+#%%%%%%%%%%%%%+:#%%%@@@@*%%%%@%@@@@@@@@@@@@@@@@@@@@@
    @@@@@@@@@@%@@@@@@%%%#%%%%%%%%#**#--:#@@%@@%%#***#%%#%%%%@@@@@@#.%%%%%#%#%%%%%%%%%%%%%%%%%%%%%##%%@@@@@%#%@%@@@@@@@@@*@@@@@@@@@@@@
    @@@@@@@@@@@@@@@@%%%%+%%#%%%%*%##**#:..@%@@=::-=:-.##+##@@@@@@@%%%+#*###*-#%%%%%%%%%%%%%%%%%%%%%%*%@@@@@%%@@@@%%#@@#+%%%++@@@@@@@@
    @@@@@@@@@@@@@@@@@%%%%#%%%#%%%:**-.==%:@@@@.#%*#%=*++%%%@@@%%#*#*.=++#*.-*+##%%%%%%%%%%%%%%%%%%%%%%@@@@@%@%%@@@@@@@@%##%@@@%@@@@@@
    @@@@@@@@@@@@@@@@%@%%%*#%#%%#%#*=.=.-%#-@@@%.%%+=##:#.#@@@@@+===+=*-=-*=-.+*#*#+##%%%%%%%+%#%%#%%%%@@@@#%@@%%@@@%@%%%=%@%@%@@@@@@@
    @@@@@@@@@@@@@%@@@%%%%%%#%%%*#%##.=#.*%@@@%..#.#@@@@@@@@@@@#+***+**+*.=++++-+-+####%%%%%%%%#+###%%%@@@@%*%%%@%%%%+%*%%+=%@#@@@@@@@ 
    @@@@@@@@@@@@@@@@@@%%%%%%@%+*%::=%#@%%%@@@%@@@@@@@@@@@@@@@##%##=+*****+=::.:...**#########%#.###%%%@@@@%%%%%%%%%%@*%%*+*+###@%@@@@
    @@@@@@@@@@@@%%%@%%%%#%%#%%%#**.#==%%%%%@@@@@@@@@@@@#+*.*########***+*+......:+**#########*+**##.**%@@@@@#%%%@%%@%%#=+***###@%@@@@
    @@@@@@@@@@@@@@@%@#%#%%%*#%%%%%.%*#%:%@@@@@@@%=%*#@%###*+.+*###*+****+=......-.++*****##*#****#+-#**@@@@@%%@@@%@@@%##*#####%@%@%@@
    @@@@@@@@@@@@%%%%#%%%%#+%%-*##%#%%+=%@@@@@@@##:#+*+#**==**#*###+.=+*++.......-==+++++***#+=.-=+*+*+*%@@@@@@@@@%%@%@@@@@@@%%%@%@%@@
    @@@@@@@@@@@@@%%@%%#%#%%###=:...=+%%@@@@@%##**%:..===.+=++.*****=--+++-......:--:===+++++=.::==-=***#@@@@%%@@@@@%@@@@@%%%%%%@%%@@@
    @@@@@@@@@@@@@@%%%%%%#%%%%##*..=%%%+@@@@@#%%+-#-...==+++.:=-:=:+*++++=-:-.....:..:--:.-=+++=.-.-+=++#%@@@%@%%@%@%@%@@%%%%%%%@%%@@@
    @@@%@@@@@@@@@@@@%%@@@%%###+####%%%%@@@@@%#=%%##.......-..:=:--+*+++.---:.........::..--:..=-=-:-==+*#@@@@*##%%%%%%%%%@@@%@%@%@@@@                                       Acabas de entrar en la selva de la isla,
    @@@@%@%@@@@@@%@@@@@@@@%%**++-=.=%**@@@@@%=.%%-........#******++=-:..::.:........:...........:..-..*=@@@@@@%@@@%%@@@%%@@@@%%@@@@@@
    @@@@@%%%@@@@@@%%@@@###@@@@@+++==%*#@@@@%*%%%-.....:###*****=-........:.........................%%*%#@@@@+*@@@@@@@@%@%@@@@@%%@%@@@                                       llena flora y fauna peligrosa, debemos tener
    @@@@%@%%%@@@@@%####*##***@@%%%**#+%@@@@%%%%#.....#*###*.*=..................................:..%+@*@@@@@@%@%%@@@@%@@%@@@@%%%@@@@@       
    @@@@%%%%%@@@@@%%##*##*#*+++%@@@@#@@@@@@%%.%.....#####*..*................................#.%%%#@@%@@@@@@+*#@%%%@%%%%%%%%@@@%@@@@@                                       cuidado de por donde pisamos para protegernos de
    @@@@@@@@%@@@@@@@%#####+==++=+%@@@@@@@*%%%.@.....####*...-...............................#%#%@@%@%@+@@@@%##%###%%#%%%%%%%@%%%@@@@@
    @@@@@@@@@@@@@@@%#***+****+:++@+%@@@%===%%%%..:.####*..:................................+%%#%%#%@%@%@@@@@*%%**#%####%%%%%@%%%@@@@@                                       los peligros que nos aguarda la jungla.
    @@@%@@@@@@@@@@@#****+##-=*+**@=%@@%--::%%%%..+####*...................................%%%%%@#%-.%#:@@@%*+=++***#####%%%%@%%%%@@@@
    @%%@@@@%@@@@@@@@***++**+=++--#@@@@*.-=:%%%%%%%###*..................................:=:-#=%+%#...**@@@@#@-++++**######%%%%%%%@@@@                                       
    @@@@%@%@@%@@@@@@@**++*==*=--:-@@@@%@@@@@%%%%%%#*+...................................#=...%%:...=@.%-@@@@:*@=++***######%%@%%@@@@@
    @@@%%%%%%##@@@@@@#+++*==-=:::.@@@@@@@@@@@%%%#........................................*..#....#+%@=.@@@@@::@==++**%@#*##%@@%@@@@@@                                       Vamos a atravesar la isla lo antes posible para
    @@@@%@%%%#@%@@@@@@++-+-==-...@@@@@@@@%%%%..%:..........................................-#....:.....@@@@...+@==++@@@#%%#@@@@@@@@@@
    @@@@@%@@%%%*+@@@@@*==#:-....@@@@@@@%.#.%%.-%.............................@@@@%.....................@@@@..:.:%=+++*@@@#@%@@@@@@@@@                                       evitar estar expuestos a los pelifros de la zona.
    @%%%%%##%*%@*+@@@@@+.*.+:..:@@@@@@-..#.%%..@.............................@@@@@@@@@@@-..............@@@@....::+=#@@@###%%@@@@@@@@@
    %@@%%####***++@@@@@:.:....=.@@@@@......%%..%.............................#.@@@@@@@@@@@%............@@@@=:..::*==+@**%@@%@@@@@@@@@                                       Para ello, nos adentraremos en ella...
    @%%%%###***++@@@@@@:....=--%@@@@@.=....%%..#=..............................=@@@@@@@@@@@@@...........@@@%....:-%++++%@@%%@@@@@@@@@
    %@%%%###*****%#@@@@-+:.-=:-@@@@@@%.....%%.#%................................@@@....=@@@@@@@.........@@@@...:::-%+++**#%@@@@@@@@@@
    %%%%####**##=*%@@@@@.:=--.*-@@@@@@.-.*:%%.#%...............................@@@#..@@@@@@@@..@=........@@@@..::--=%++*@%*@@@@@@@@@@                                       Pulsa Enter para continuar.
    %%%%###%@#**@@*@@@@@:.....@%@@@@@=:..-.%%.%%.............................%@..@...@@...@@@...%@.......@@@@@:::---@+*+%*@@@@@@@@@@@
    %%%%%@@@%@@@@@@@@@@@-.....@@@@@@%#.....%%.:%................::...........%=..@...@@=.@@@......@......@@@@@.::=%=@###%@%@%@@@@@@@@
    %%%%%@@@@@@@@@@@@@@@*=*..#@@@@@@-......:%.#%....................-.---.+**#...@..+.@@.@@@.......@.....@@@@@:::-%##%%%@@@%@%@@@@@@@
    @@@@@%@%#@@@@@+@@@@@%%-:%%@@@@@@+......@%.*%................##*.:=**####%%%%%@@@@@%...%%@+......@....@@@@@::--==+@%@@@@@@@@@@@@@@
    @@@@@@@%####**#@@@@@@-@=.@@@@@@@.#.....@%.@@..%............#..**##.%%%%%%%%@@@@@@@@@@@@@%@@.....=-...@@@@@@@-%#+%%@%@@@@@@@@@@@@@
    @@@@%@%@%##@%#@@@@@@@#@@@@@@@@@@.-....%@..@@@@%%.:%.%.......=.....%%%%%%%@@@@@@@@@@@@@@@@@@@.@-.%...@@@@@@@@@*#%@%@%@@@@@@@@@@@@@
    @@@@@@%%%@%@%%%@@@@@@#===@@@%@@@%-....+%@@%:@@%.%%%................+%@@@@@@@@@@@@@@@@@@@@@@@@@@:..=@@@@@@%@@@@@@@@%@@@@@@@@@@@@@@
    @@@@@@@%@%%@@%@@@@@@@%*==@@@@@@@=:...@@%#.@#%%@@:@.:............%.%@*%@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%@%@@@@@@@@@@@@@@@@@@@@
    @@@@@@@@%%%%##@@@@@@##*++@@@%@@@@@::@@%@@:@.:%%@%.............%%#.%@%%%@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
    @@@@@@@@%%%%#%@@@@@@#***@@@@%@@==@@@@%@@..%.-..%+.............%%#...%#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
    @@@@@%@@%@%@%@@@@@@@@##*@@@@@@@@@%*%--%@%%%:+#=#............+:.:%@*@*.@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
    @@@@@@%%@%%@%@@@@@@@@@##@@@@@@@%@@@+##%=#=@-#..=...............%%.....%..@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
    @@@@@@@%%%@@@@@@@@@@@#%@@@@@@@@%@%%*%*@@@@%@+-:....................=.%#:..%%.*.%@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
    @@@@@@@@%@@@@@@@@@@@@@@@@@@@@@@%******@#%*#@@%*-....................=..%..%=..*@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
    @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@####%*#*#%#*@**+#+*=................+@.:..@-#::@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
    @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@#%%######@*%%%%%%%#.................=@.%..@@=--@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
    @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%%###%#@%@#%%#@@%=:.:..............%.:*:@@+-=@*@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
    @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%%%%%%%##@#%#%%**+:--..............*:-%:+%+++#*@@@@%#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
    @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%%%%%@#%#@###***+=................@:#:+++*+**@@@@@%%@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
    @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@#%%@%%%%%%###***+..............+:=-#@@**@**@@@@@@@@@@@@%@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
    @@@@@@@@@@@@@@@@@@@@@@@@@@@%@@@@@#@@%@@%%%%%%%#####**+-.........:::--*=#@#*##@@%@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
    @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%@%%@@=%%%%%####***=:::::::::----%++@*@@@@@##@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
    @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%@@@@@@%@#%%%%*#####*---:::-----==@#*@#@#@@%%@@@%@@%@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
    @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%%%%##+####**=----====+++@#*@@@@@%@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
    @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%@@=@@@@@+%%%%####%#+**+===++++*@#%%*@@@@@@@@@%@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
    @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@+@@%%%@@@@%%%%%######*#++++=*+%%%=@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@""")

    input()

    texto3="""
    \n\n\n\n\n\n
    \t\t\t\t\t\t\t\t\t\t\t\tDespués de estar media hora recorriendo la selva... 
    \n\n\t\t\t\t\t\t\t\t\tPulsa Enter para continuar:
    """

    os.system("cls")
    
    for _ in texto3:
      print(_, end="", flush=True)
    
      if _!="\t" and "\n":
        time.sleep(0.04)

    input()

    os.system("cls")

    print("""
    @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@+@@@@@@@@@@@@@@@@--@:@:@@@:@+:@@:@@@@-@@@@@@@@@@@@@%@@@@@@@@@@@@@@@@@@@@@@@@@@@
    @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@=@@@@@@@@@@@@@:@::@:-@@@@:#@:+@:@@@:@*@@@@@@@@@@-@@@=@@@%%%@@@#@@@%@@@@@@@@@@@@
    @@@@@@@@@@@@@@#@@*+#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%@#@=@@@@@@@@@@@:@@::*+:-#@@::@::@:@@:::@@@@@:*=@@@@@-@@@=@@##%*%=+@@%+@@@@@@@@@@@@
    @@@@@@@@@@@@@*%%@***@@*@#@@@@@@@@@@*@@@@@@@@@@@@@@@##*+-#@@@@@@@@@@*:::@::-@@=::::::@:::@@@:::-@@@@@@@@--@@-=@*++===+@@@@@@@@@@@@@@@@
    @@@@@@+@@@@@@@@@@@@@@@+@%@@@@@@@@@@@@@@@%@@@@@@@@@@@@=--::#@-@@@@@@::+::::@@:::::@:::::@:::-:@@@@:@@@@@-:--@-@@*==+=@@@@@@@@@@@@@@@@@
    @@@@@@@@@@@@@@@@@@@@@@@@@@@@%*@@@@@@=@@@-@@@@*@@@@@--@@-::::::*@@@::@:@:::-:::-::::::::::::%@@=:@:@@@:@@::-:-@+:-@@@@@@@@@@@@@@@@@@@@
    @@@@@@@@@@@#*@----@@@@@@@@@@-@@@@@@@%@@@+@@@@:@@@@@@@:::::::::@::-@::::@::%::::@@::::::::=@+::::%:@:@:@@:::::@*-@@@@@@@@@@@@@@@@@@@@@
    @@@+@@@@@*==+=@:-:+--@*@@@@@@-+@@@@@@@@:=@+@@=@@@@*@:::::::::::-::::::::::=@::::::::::@:::::::::::-:@::@:::::+@@@@*@@@@@@@@@@@@@@@@@@
    @@@=@@@@@@@@++=---=:::@@@@:=@@@:@@@@@@@@@:::@@@@@@@@@::::::::::::::::::::%::::::::::::::::::::::::::@::::::::@@@@@@@@@@@@@@@@@=@*@@@@
    @@@@@@@@=--:-:%@@@=+::@@@::=@*::@@@@@@@@@::::::@@@@@%::::::::::::::::::::::::@:::@#@::::::::::::::::@:::::::@@@@@@@@@@@@@@-@@@+@-%@@@
    @@=@@@@@@@@@=::::-::::@@=@@-:+*%@@@@@@*@@@:::*:::@@@@#:::::::::::::::::::@:::::::::::::::-@::::::@=:@::::::@@@*@@@@@@@@@@@@@@#-@-+@@@
    -@-@@@@@=:-%=::::=@@@@@%:::=:@@:::@@@@@@@@-:::::+::-@::::::::@::::::::::::::::::::::::::::::::::::::-:::::@@@@@@@@@@@@@@@::@@@::+:@@@
    @@@@@@@@-::::::@@@@:+@@::@*:@::::::@@@@%@@%:#::::::::::::::::::::::::::::::::::::::::::::::::::*:::::@%-:@@@@@@@@@@@@@#:-@:@@=:-*-@@@
    @@@@@@@@::::@@@::@@:@@@@@@::::#::#::@@@:@@@@::::::::::::::::::::::::::::::::::::--:::::@%::::-:::::::@:::@@@@@-@@@@:::=::::@@@::@*:@@
    @@@@@@#*@@@@::::=@@@@@@::::#::+::::::++::@@%:::::::::::::::::::::::::::::::::::::::::::::::::::::::::@::@@@@@@:@:::::::*:::@@@::=@@@@
    @@@@@@@@@-::::=::-#@@@@:@+:::::::::::::::@@@::::::::::::::::::::+@:::::::::::::::::::::::::::::::::::-::@@#@#:::::::@::@:::#@@@@@@@@@
    @@@@@@@@@@:::#@@@@@@@@@@@:::::::@::::::::@@@@:::::::::::::::::::::::::::::::::::::::::::::::::::::::::@:-+:::::@@#:::::+::@@@@@@@@@-@                                 
    @@@@@@@@@@%@@@:::@@@+@@@@@@#:::::::::::::::@@::::::::::::::::::::::::::::::::::::::@::::::*-::::::::::@:::@:::@:::::::%=@@@@@@@:@@:@@
    @@@@@@@@@@@+=@-##@@@*@::::@@@:::::::::::::::+:::::::::::::::::::::::::::::::::::::::::::::::::::::::::*::::::::::::::*@::@@:@@:*::=-@                                 
    @@@@@@@@@@%%%%##@@@#*+**::::::::::::::::::::::::::::::::::::+-:@@%@:-=-::::::::::::::::::::::@@::::::::@::::::::::::%::-@-:-@:::::::-
    @@@@@@@@@@@@*@@@@@@#@*=#%=::-:=::::::@::::::::::::::::::=@@@@@@@@@@@@@@@+*@-@@:=:::::::::::::::::::::::@:::::::::::=#%:#:::=@::@:#:::                                       
    @@@@@@@@@@@@#@@@@@@%#%-%%%@----+-::::::::::::::::::::-@@@@@@@@@@@@@@@@@@@@@@@@@@@-::::::::::::::::::::::@::::::::::::::@::=:@:-@::@=:                                 
    @@@@@@@@@@@#@@@@@@@@@#%%@%@%:---=::::::::::::::::::*@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%:::::::::::::::::::@:::::-:--:::::@----@::-:-:@@
    @@@@@@@@@@@@@@@@@@@@%%%@@@@@%-+=--::::::::::::::::#@@@@@@@@@@::::::::::@@@@@@@@@@@:@@@@-:::::::::::::::::*::---=%----=-@--=-@-@-=@@@@                                 Se nos ha aparecido una serpiente y
    @@@@@@@@@@@@@@@@@@#@@@%@-@@%%%#*=+*-:::::::::::::-@@@@@@@@@:::::::::::::::@%@@@@@@@@@@@@@:::::::::::::::::-----=-@==---+---:@::=@@@@@
    @@@@@@@@@@@@@@@@@@%@@%%%%:%#@@##*+**:::::::::::::@@@@@@@@::::::::::::::::::::::::@@@@@@@=:::::::::::::::::==---=====-+-:::+-@@@@@@@@@                                 nos ha bloqueado el paso.
    @@@@@@@@@@@@@@@@%@%%@%%@%@#@@%#%###+#::::@:::::::@@@@@@@#:::::::::::::::::::::::::::::::::@@::::-:::-----=-%-===-----:::==:@@@@@@@@@@
    @@@@@@%@@@@@@@#@%@@%%@%@@%%%%@*@@##-##:::::::::::@@@@@@@@::::::::::::::::::::::::::::::::::::::::::-=-:---==@--=---:::@*-%@@@*:-:@@@@                                 Abre el menú para ver que podemos hacer.
    @@@@@@@@@@@%#%@%%%@%%###%%##@@%@@=@=##:::::::::::@@@@@@@@-:::::::::::::::::::::::::::::::::::::::=+--=:-:===-=-::-:@@@@@@@@@@@@@@@*=@
    @@@@@@@@@@#@%##%#%#####%#####%%#%%@@-%#:::::::::::@@@@@@@@@-:::::::::::::::::::::::::::::::::::-++===-=:+++::-::::@@@@@@@@@@@@@@@@@@@
    @@@@%@@%###*#**********#***%+%#%@%%%@%%@::::::::::*@@@@@@@@@@+#=::::::::::::::::::::::::::::::====-++:=+=-::::::::@@@@@@@@=@@@%@@@@@@
    @@@@@@***@@@@@@@@@@@@:*+*#:##*#:#%%+@%@@@=::::::::::@@@@@@@@@@@@@@@##-:::::::::::::::::::::::-:=++-+-+=:-==-::::@@+@@@@@:@@@@#@@@@@@@
    @@+#*@@@@@@@@@@@@@@@@@@@*+*+***#:**%-#%%%-@::::::::::-@@@@@@@@@@@@@@@@@@@-::::::::::::::::::-==+:==+=:=:--:::::@@@@%@@@@@@@@@+@@@%@@@
    @@@@@@@@@@@@+#@@@@@@@@@@@+++=+=+*+*=**#*@@:@@:::::::::::*@@@@@@@@@@@@@@@@@@=:::::::::::::::-=+===:-::-::::@@@@@@@-@@@:@@@@@@@@@%@@@@@
    @@@@@@@@@***+=#%##@@@@@@@@+=====+*-+++#:#-%:@@:::::::::::::::-@@@@@@@@@@@@@@@::::::::::::--=-===-:::::::@@@@@@@@@@@:@@@@@@@@@*@@@@@@@
    @@@@@@@=+@*@@@%@@@@@@@@@@@@@=--======+==:*-%%%@-:::::::::::::::::::@@@@@@@@@@@:::::::::::--+==::-:::@:@@@@@@%@@@@:@@@@@@@@-@@@-@@@@@@
    @@@@@@@@@@@@@@@@@@@@@@@@#%@@@@@@-=-===--=-==++%#%%:::::::::::::::::::@@@@@@@@@%::::::-:=----:-::#@@@@@@@@@@@@@@:@@@@#@+@:*@+@@@@@@@@@
    @@@@@@@@@@@@@@@@@@@@@@@@@@*@@@@@@@---=-=-==::-+**#%%%:::--:::::::::::+@@@@@@@@@:::-----=-::::::@@@@@@@@@@@@*##*%%%@@-#:#::*@@@@@@@@@@
    @@@@@@@@@@@#=@#@=@-@@%@@@@@@-@@@@@@+=----------:==**#%=::::::::::::::=@@@@@@@@@::----:::::::--:@@@@@@@@@@#-#+##@*@%*:+-:%@@@@@@@@@@@@
    @@@@@@@@@@@@+@@---=+-=+*#%%%@%%@%%@@=#::-----::-=:==-+*+#=:::::::::#*@@@@@@@@@::::::-:::---:::@@@@@@@@*#%+*=#=*:*=:-:@@@@@@@@@@@+@@@@
    @@@@@@@@@@@@@@@@@#=*-+=-+=++***+**###=+::-::::::---:--===+==::::*#@=@@@@@@@@@-:::::::-:--:::@@@@#%%#*%+==+=-:-::@@@@@@@@@@@@@@@@%@@@@
    @@@@@@@@@@@@@@@%=:--:--=::#@@@@@@@@@@%##::::::::::::-:::----==%@@@@@@@@@@@@@:----:::--:-:+#+=#*-:=*:=-+-=:::@@@@@@@@@@@@@@@@@@@@@@#@@
    @@@@@@@@@@@@@@@@@-@*:*-:@@@#-==+****@@@#*%:::::::::::::=*@@*@@@@@@@@@@@@@@@-::::::::::-*+-:=::-:=-=--:::::@@@@@@@@@@*=@@%@+@@@@@@@@@@
    @@@@@@@@@@@@@@@@@@@*#-=@@--::::::-+++@@@##+@@@%%%:::#@@@@@@@@@@@@@@@@@@@*::::::::::::=-:---::-:---:::::-@@@@@@@@@:-@@@@@@@@#@@@@@%@@@
    @@@@@@@@*====@=@@-:@=@@@=@@@@@@=+=::--@@@+####**%#**@@@@@@@@@@@@@@@@@-::::::+=@@+%@@##-#:-:::::::::::::@@%*%#%@#:@*++=+=-=+=@-%#@@@@*
    @@@@@@@@@@@@%+-=%+@@@:-::-+:##@@*----:@@@++=+++*@@@@@@@@@@@@@@@@@+::::::@=@@@@@@@@@@@@@@@@+@:::::::%@@#-++=@@-=-#==+-+@-:-@-+#@*@@@@@
    @@@@@@@@@@@@@@@@@@@:@@@:@@:::--=@@:::-@@*::-=-@@@@@@@@@@@@@@@@::+*+=#*+@@@@@@@@@@@@@@@@@@@@*@@:=**@%##::::::#+-:--@@@@@@@@=--=@*@@@@@
    @@@@@@@@@@@@@@@@@@@@@@@@@@@@@:---=+::@@@:::::@@@@@@@@@@@@@@::::-::=@#@@@@@@@@@@@@@@@@@@@@@@@@@@@=++*=::=:::::==@@@@@@@@@@@@@@+*+*@@@@
    #@@@@@@@@@@@@@@@@@@@@@@*@@@@@@:::-::@@@:::::@@@@@@@@@@@@@:::::::@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@-----+=:::*@@@@-:::@%@@@@@@@@%@@#@@@
    @@@#@@@@@@@@@@@@@@@@@@@@@@@@#@@@:::@@@:::::@@@@@@@@@@@@@:::::::@@@@@@@@@@@@@::::::::-@@@@@@@@@@@@@::::-=+-@=-*-+:::-::=@@@@@@@@@@%+@@
    @@@#@@@@@@@:@@@@@@@@@@@@@@@@#::-:%@@@-:::::@@@@@@@@@@@@:::::::@%@@@@@@@@@:::::::::::::@@@@@@@@@@@@::::+-=:-:-=-*:::@@@@@@@@@@@@@@@@#@
    %@@@@@@@@@@@-@@@@*@@+##@@@@@-@@@@@@@@@@@::@@@@@@@@@@@@*::::::@@@@@@@@@@@:::::::::::+-::@@@@@@@@@@@:::*:@@*:-#=--+@@@#@*@*@@@@@@@@@@%@
    @@@@@@@@@@@=@@@@@#@@@@@@@@@@@=#@-@@@::::-:@@@@@@@@@@@@@:::=:#@@@@@@@@@@:::::%*-@@%%:@:@@@@@@@@@@@@-:@@@@@@-@=#+-@@%=@@#@@@@@@@@@:@#@@
    @@@+@@@@@@@@@@@@@@@@@-:@@#@@@@@@@@@@::::-=@@@@@@@@@@@@@:@=@:@@@@@@@@@@*:@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@*@=*%==**@*#@#@@@*@@@@:-@-:@@
    @@@@@@@@@@@@@@@@@@@@@@@@#@@@@@@@@@@@@:::-:@@@@@@@@@@@@@@@@-:@@@@@@:-@@@@%@@@@@@@@@@@@@@@@@@@@@-@@@@@@@@@@@@@==%+*#@=@@@@@@@@-=@-:@@@@
    @@@@*@@@@@@@@@@@@@@@@@@%@@@@@%=@+@@@@@--@:@@@@@@@@@@@@@@@@+@@@@@+@@@@@@@@@@@@@@@@@@@@@@@@@-=@@@@@@@@@@@@@@@@@@###+@@@@*@-@@@@=@@@@@@@
    @@@@@@@@@@@@@@@@@@@@@@@@@%@=@%*@==@@@@@@:-@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@+#+@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%#@@@@@@@@
    @@@@@@@@@@@@@@@@@@-:+@@@@@%@@%@@@@@#*@@@=@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%-@@@@@@@@@@@@@@@##@@%@@@@@@@@@+@@@@-@*@@@+@@@@@@@@@@
    @@@@@#@@%@@@@@@@@@@@@@@-=@*:-@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@-@:#@@@@@@@@@@@@@@@@@*@@@:-=@@@@@@@@@@@+@@@@@#@@@@@@@#@@@
    @-@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@=#:@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%@@*@@@@@@@+@@@@@@@@@@@@@@@@=@@@@@
    @@@@@@@@@@@@@@@@@@@@@@@@*@@@@@@@@@@@@@@@@@@@@@@@#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@=#@@@@@@%@@@@@@@@@@@@@@@@@#@@@@@@*%
    @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@+-@@@
    @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@+-@@@""")




    while serpiente_v==True:

        opc_menu=input(f"\n{Fore.LIGHTWHITE_EX}Pulsa 'm' y Enter para abrir el menú: ")

        if opc_menu=="m":
          os.system("cls")

          print(serpiente_menu)
          print(acciones)
            
          print("|  Indica la acción que quieres realizar: ")
          opcion_acc=input("|       --> ")
          

          match opcion_acc:
              case "1":
                  os.system("cls")
                  print(serpiente_menu)
                  print(coger_intf)
                  opcion_coger=input("       --> ")
                  print("Ahora mismo no hay nada que coger")
                  input("Pulsa Enter para continuar")


              case "2":
                  os.system("cls")
                  print(serpiente_menu)
                  print(usar_intf)

                  for i in list(objetos):
                      contador_objetos+=1
                      print(contador_objetos, objetos[contador_objetos-1])
                  contador_objetos=0

                  opcion_usar=input("       --> ").lower()

                  if opcion_usar=="antorcha con serpiente" or opcion_usar=="antorcha":
                      os.system("cls")
                      print(serpiente_menu)
                      print(usar_intf)
                      print("Enhorabuena, el fuego de la antorcha ha hecho que la serpiente huya y nos ha dejado la vía libre.")
                      input("Pulsa cualquier botom para continuar.")
                      serpiente_v=False

                    
                  else:
                    print("Esos objetos no se pueden usar")
                    input("Pulsa Enter para continuar")


              case "3":
                  os.system("cls")
                  print(serpiente_menu)
                  print(dar_intf)

                  for i in list(objetos):
                      contador_objetos+=1
                      print(contador_objetos, objetos[contador_objetos-1])
                  contador_objetos=0

                  opcion_dar=input("       --> ").lower()

                  print("No puedes dar este objeto")
                  input("Pulsa Enter para continuar")


              case "4":
                  os.system("cls")
                  print(serpiente_menu)
                  print(inventario_intf)

                  for i in list(objetos):
                      contador_objetos+=1
                      print(contador_objetos, objetos[contador_objetos-1])
                  contador_objetos=0

                  input("\nPulsa Enter para continuar")

              case _:
                print("Lo siento, está opción no está contemplada")   

        else:
            print("Lo siento, está opción no está contemplada")   


    os.system("cls")

    texto3="""
    \n\n\n\n\n\n
    \t\t\t\t\t\t\t\t\t\t\t\tDespués de estar 1 hora recorriendo la selva... 
    \n\n\t\t\t\t\t\t\t\t\tPulsa Enter para continuar:
    """
    for _ in texto3:
        print(_, end="", flush=True)
    
        if _!="\t" and "\n":
            time.sleep(0.04)

    input()

    os.system("cls")  

    print("""
@@@@@@@@@@@@@@@@@@@%@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%@%:+%@@@@%%%#*%#%%*%#@*@@@@%%@@%@%%%@%@@@%%@@@@%%@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@%@@@@@@@@@@@%%@@@@@@@@@@@@@@@@@@@@@@#%@@@%%%*=#%%#%%%%%%%@*@@@@@@@%*-%@@@@%@@@@@@@%#@@@%@@%%%%%@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@%%@@@@%@%@%%%@@@@@@@%%@%@@@@@@%%@#@@@@.*@#%%--:%#%%%#%@@@%%%%%%@@%@%@@@@@@@@@@@%@@@%@@@@%@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@%#%%%%%%%%%@%@%@@%@%%%@@@@@@%%%@@@:..*-%%#%%%@%%%%%%%%%%%%*%%%%%%@#%%%%%@@@@%%%%%@%@@@@@@@@@@@@@@%@@@@@@
@@@@@@@@@@@@%@@@@@@@@@@@%%%%%%%%%###%%%@@@%%%%%%%%%@%%%%@@@:..++%%%%%%@%%%%%%%%%%%%%%@%%%%%%+*%%%@@@@#%%%@@@@@@%%@@@%@@@@@@%@@@@@
@@@@@@@@@@@@@%@@@@%%%@%%@%%%%%%%###+*%@@%%###%%%%%%%%%%%@@@%%#%%%%%%%%%%%%%%+#%%%%%%%%%%%%%+:#%%%@@@@*%%%%@%@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@%@@@@@@%%%#%%%%%%%%#**#--:#@@%@@%%#***#%%#%%%%@@@@@@#.%%%%%#%#%%%%%%%%%%%%%%%%%%%%%##%%@@@@@%#%@%@@@@@@@@@*@@@@@@@@@@@@
@@@@@@@@@@@@@@@@%%%%+%%#%%%%*%##**#:..@%@@=::-=:-.##+##@@@@@@@%%%+#*###*-#%%%%%%%%%%%%%%%%%%%%%%*%@@@@@%%@@@@%%#@@#+%%%++@@@@@@@@
@@@@@@@@@@@@@@@@@%%%%#%%%#%%%:**-.==%:@@@@.#%*#%=*++%%%@@@%%#*#*.=++#*.-*+##%%%%%%%%%%%%%%%%%%%%%%@@@@@%@%%@@@@@@@@%##%@@@%@@@@@@
@@@@@@@@@@@@@@@@%@%%%*#%#%%#%#*=.=.-%#-@@@%.%%+=##:#.#@@@@@+===+=*-=-*=-.+*#*#+##%%%%%%%+%#%%#%%%%@@@@#%@@%%@@@%@%%%=%@%@%@@@@@@@
@@@@@@@@@@@@@%@@@%%%%%%#%%%*#%##.=#.*%@@@%..#.#@@@@@@@@@@@#+***+**+*.=++++-+-+####%%%%%%%%#+###%%%@@@@%*%%%@%%%%+%*%%+=%@#@@@@@@@ 
@@@@@@@@@@@@@@@@@@%%%%%%@%+*%::=%#@%%%@@@%@@@@@@@@@@@@@@@##%##=+*****+=::.:...**#########%#.###%%%@@@@%%%%%%%%%%@*%%*+*+###@%@@@@
@@@@@@@@@@@@%%%@%%%%#%%#%%%#**.#==%%%%%@@@@@@@@@@@@#+*.*########***+*+......:+**#########*+**##.**%@@@@@#%%%@%%@%%#=+***###@%@@@@
@@@@@@@@@@@@@@@%@#%#%%%*#%%%%%.%*#%:%@@@@@@@%=%*#@%###*+.+*###*+****+=......-.++*****##*#****#+-#**@@@@@%%@@@%@@@%##*#####%@%@%@@
@@@@@@@@@@@@%%%%#%%%%#+%%-*##%#%%+=%@@@@@@@##:#+*+#**==**#*###+.=+*++.......-==+++++***#+=.-=+*+*+*%@@@@@@@@@%%@%@@@@@@@%%%@%@%@@ 
@@@@@@@@@@@@@%%@%%#%#%%###=:...=+%%@@@@@%##**%:..===.+=++.*****=--+++-......:--:===+++++=.::==-=***#@@@@%%@@@@@%@@@@@%%%%%%@%%@@@
@@@@@@@@@@@@@@%%%%%%#%%%%##*..=%%%+@@@@@#%%+-#-...==+++.:=-:=:+*++++=-:-.....:..:--:.-=+++=.-.-+=++#%@@@%@%%@%@%@%@@%%%%%%%@%%@@@
@@@%@@@@@@@@@@@@%%@@@%%###+####%%%%@@@@@%#=%%##.......-..:=:--+*+++.---:.........::..--:..=-=-:-==+*#@@@@*##%%%%%%%%%@@@%@%@%@@@@                                       ¡Vaya!, hemos vuelto al mismo punto de antes,
@@@@%@%@@@@@@%@@@@@@@@%%**++-=.=%**@@@@@%=.%%-........#******++=-:..::.:........:...........:..-..*=@@@@@@%@@@%%@@@%%@@@@%%@@@@@@
@@@@@%%%@@@@@@%%@@@###@@@@@+++==%*#@@@@%*%%%-.....:###*****=-........:.........................%%*%#@@@@+*@@@@@@@@%@%@@@@@%%@%@@@                                       parece que estamos perdidos en la jungla,
@@@@@@@@%@@@@@@@%#####+==++=+%@@@@@@@*%%%.@.....####*...-...............................#%#%@@%@%@+@@@@%##%###%%#%%%%%%%@%%%@@@@@
@@@@@@@@@@@@@@@%#***+****+:++@+%@@@%===%%%%..:.####*..:................................+%%#%%#%@%@%@@@@@*%%**#%####%%%%%@%%%@@@@@                                       encuentra la manera de salir de ella.
@@@%@@@@@@@@@@@#****+##-=*+**@=%@@%--::%%%%..+####*...................................%%%%%@#%-.%#:@@@%*+=++***#####%%%%@%%%%@@@@
@%%@@@@%@@@@@@@@***++**+=++--#@@@@*.-=:%%%%%%%###*..................................:=:-#=%+%#...**@@@@#@-++++**######%%%%%%%@@@@                                       
@@@@%@%@@%@@@@@@@**++*==*=--:-@@@@%@@@@@%%%%%%#*+...................................#=...%%:...=@.%-@@@@:*@=++***######%%@%%@@@@@
@@@%%%%%%##@@@@@@#+++*==-=:::.@@@@@@@@@@@%%%#........................................*..#....#+%@=.@@@@@::@==++**%@#*##%@@%@@@@@@                                       De momento no hay mucho a nuestro alrededor,
@@@@%@%%%#@%@@@@@@++-+-==-...@@@@@@@@%%%%..%:..........................................-#....:.....@@@@...+@==++@@@#%%#@@@@@@@@@@
@@@@@%@@%%%*+@@@@@*==#:-....@@@@@@@%.#.%%.-%.............................@@@@%.....................@@@@..:.:%=+++*@@@#@%@@@@@@@@@                                       solamente árboles, palmeras, bichos y
@%%%%%##%*%@*+@@@@@+.*.+:..:@@@@@@-..#.%%..@.............................@@@@@@@@@@@-..............@@@@....::+=#@@@###%%@@@@@@@@@
%@@%%####***++@@@@@:.:....=.@@@@@......%%..%.............................#.@@@@@@@@@@@%............@@@@=:..::*==+@**%@@%@@@@@@@@@                                       un mono comiendo insectos.
@%%%%###***++@@@@@@:....=--%@@@@@.=....%%..#=..............................=@@@@@@@@@@@@@...........@@@%....:-%++++%@@%%@@@@@@@@@
%@%%%###*****%#@@@@-+:.-=:-@@@@@@%.....%%.#%................................@@@....=@@@@@@@.........@@@@...:::-%+++**#%@@@@@@@@@@
%%%%####**##=*%@@@@@.:=--.*-@@@@@@.-.*:%%.#%...............................@@@#..@@@@@@@@..@=........@@@@..::--=%++*@%*@@@@@@@@@@                                       
%%%%###%@#**@@*@@@@@:.....@%@@@@@=:..-.%%.%%.............................%@..@...@@...@@@...%@.......@@@@@:::---@+*+%*@@@@@@@@@@@                                       Pulsa 'm' para abrir el menú
%%%%%@@@%@@@@@@@@@@@-.....@@@@@@%#.....%%.:%................::...........%=..@...@@=.@@@......@......@@@@@.::=%=@###%@%@%@@@@@@@@
%%%%%@@@@@@@@@@@@@@@*=*..#@@@@@@-......:%.#%....................-.---.+**#...@..+.@@.@@@.......@.....@@@@@:::-%##%%%@@@%@%@@@@@@@
@@@@@%@%#@@@@@+@@@@@%%-:%%@@@@@@+......@%.*%................##*.:=**####%%%%%@@@@@%...%%@+......@....@@@@@::--==+@%@@@@@@@@@@@@@@
@@@@@@@%####**#@@@@@@-@=.@@@@@@@.#.....@%.@@..%............#..**##.%%%%%%%%@@@@@@@@@@@@@%@@.....=-...@@@@@@@-%#+%%@%@@@@@@@@@@@@@
@@@@%@%@%##@%#@@@@@@@#@@@@@@@@@@.-....%@..@@@@%%.:%.%.......=.....%%%%%%%@@@@@@@@@@@@@@@@@@@.@-.%...@@@@@@@@@*#%@%@%@@@@@@@@@@@@@
@@@@@@%%%@%@%%%@@@@@@#===@@@%@@@%-....+%@@%:@@%.%%%................+%@@@@@@@@@@@@@@@@@@@@@@@@@@:..=@@@@@@%@@@@@@@@%@@@@@@@@@@@@@@
@@@@@@@%@%%@@%@@@@@@@%*==@@@@@@@=:...@@%#.@#%%@@:@.:............%.%@*%@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%@%@@@@@@@@@@@@@@@@@@@@
@@@@@@@@%%%%##@@@@@@##*++@@@%@@@@@::@@%@@:@.:%%@%.............%%#.%@%%%@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@%%%%#%@@@@@@#***@@@@%@@==@@@@%@@..%.-..%+.............%%#...%#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@%@@%@%@%@@@@@@@@##*@@@@@@@@@%*%--%@%%%:+#=#............+:.:%@*@*.@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@%%@%%@%@@@@@@@@@##@@@@@@@%@@@+##%=#=@-#..=...............%%.....%..@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@%%%@@@@@@@@@@@#%@@@@@@@@%@%%*%*@@@@%@+-:....................=.%#:..%%.*.%@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@%@@@@@@@@@@@@@@@@@@@@@@%******@#%*#@@%*-....................=..%..%=..*@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@####%*#*#%#*@**+#+*=................+@.:..@-#::@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@#%%######@*%%%%%%%#.................=@.%..@@=--@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%%###%#@%@#%%#@@%=:.:..............%.:*:@@+-=@*@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%%%%%%%##@#%#%%**+:--..............*:-%:+%+++#*@@@@%#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%%%%%@#%#@###***+=................@:#:+++*+**@@@@@%%@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@#%%@%%%%%%###***+..............+:=-#@@**@**@@@@@@@@@@@@%@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@%@@@@@#@@%@@%%%%%%%#####**+-.........:::--*=#@#*##@@%@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%@%%@@=%%%%%####***=:::::::::----%++@*@@@@@##@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%@@@@@@%@#%%%%*#####*---:::-----==@#*@#@#@@%%@@@%@@%@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%%%%##+####**=----====+++@#*@@@@@%@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%@@=@@@@@+%%%%####%#+**+===++++*@#%%*@@@@@@@@@%@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@+@@%%%@@@@%%%%%######*#++++=*+%%%=@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@""")     





    while selva_v==True:

        opc_menu=input(f"\n{Fore.LIGHTWHITE_EX}Pulsa 'm' y Enter para abrir el menú: ")

        if opc_menu=="m":
          os.system("cls")

          print(selva_menu)
          print(acciones)
            
          print("|  Indica la acción que quieres realizar: ")
          opcion_acc=input("|       --> ")
          

          match opcion_acc:
              case "1":
                  os.system("cls")
                  print(selva_menu)
                  print(coger_intf)
                  opcion_coger=input("       --> ")
                  print("Ahora mismo no hay nada que coger")
                  input("Pulsa Enter para continuar")


              case "2":
                  os.system("cls")
                  print(selva_menu)
                  print(usar_intf)

                  for i in list(objetos):
                      contador_objetos+=1
                      print(contador_objetos, objetos[contador_objetos-1])
                  contador_objetos=0

                  opcion_usar=input("       --> ")
                  print("Esos objetos no se pueden usar")
                  input("Pulsa Enter para continuar")


              case "3":
                  os.system("cls")
                  print(selva_menu)
                  print(dar_intf)

                  for i in list(objetos):
                      contador_objetos+=1
                      print(contador_objetos, objetos[contador_objetos-1])
                  contador_objetos=0

                  opcion_dar=input("       --> ").lower()


                  if opcion_dar=="banana a mono" or opcion_dar=="banana":
                      os.system("cls")
                      print("""                 
                                
                                                                                                                 __,__
                                                                                                        .--.  .-"     "-.  .--.
                                                                                                       / .. \/  .-. .-.  \/ .. \\
                                                                                                      | |  '|  /   Y   \  |'  | |
                                                                                                      | \   \  \ 0 | 0 /  /   / |
                                                                                                       \ '- ,\.-"`` ``"-./, -' /
                                                                                                        `'-' /_   ^ ^   _\ '-'`
                                                                                                        .--'|  \._ _ _./  |'--. 
                                                                                                      /`    \   \.-.  /   /    `\\
                                                                                                     /       '._/  |-' _.'       \\
                                                                                                    /          ;  /--~'   |       \\
                                                                                                   /        .'\|.-\--.     \       \\
                                                                                                  /   .'-. /.-.;\  |\|'~'-.|\       \\
                                                                                                  \       `-./`|_\_/ `     `\'.      \\
                                                                                                   '.      ;     ___)        '.`;    /
                                                                                                     '-.,_ ;     ___)          \/   /
                                                                                                      \   ``'------'\       \   `  /
                                                                                                       '.    \       '.      |   ;/_
                                                                                                     ___>     '.       \_ _ _/   ,  '--.
                                                                                                   .'   '.   .-~~~~~-. /     |--'`~~-.  \\
                                                                                                  // / .---'/  .-~~-._/ / / /---..__.'  /
                                                                                                 ((_(_/    /  /      (_(_(_(---.__    .'
                                                                                                           | |     _              `~~`
                                                                                                           | |     \'.
                                                                                                            \ '....' |
                                                                                                             '.,___.'""")
                          
                      texto4="""\n\n\n
\t\t\t\t\t\t\t\t\t\t\tGenial, parece que nos hemos ganado la confianza del mono \n\n\t\t\t\t\t\t\t\t\t\t\t\t   y nos ayudará a salir de la selva,\n\n\t\t\t\t\t\t\t\t\t\t\t         vamos a seguirlo a ver a donde nos lleva.
\n\n\t\t\t\t\t\t\t\t\t\t\tPulsa Enter para continuar con la historia."""

                      objetos.remove(". Banana")

                      for _ in texto4:
                        print(_, end="", flush=True)
    
                        if _!="\t" and "\n":
                            time.sleep(0.04)

                      input()

                      os.system("cls")
                      selva_v=False 

                  else:       

                    print("No puedes dar este objeto")
                    input("Pulsa Enter para continuar")


              case "4":
                  os.system("cls")
                  print(selva_menu)
                  print(inventario_intf)

                  for i in list(objetos):
                      contador_objetos+=1
                      print(contador_objetos, objetos[contador_objetos-1])
                  contador_objetos=0

                  input("\nPulsa Enter para continuar")

              case _:
                print("Lo siento, está opción no está contemplada") 
                    

        else:
            print("Lo siento, está opción no está contemplada")


    pygame.mixer.music.stop()
    retorno=1
    retorno_back=0

    for i in range(9):
      mapa_anim=mapa.replace(f"{b}{b}", f"{personaje_unicode}{mono_unicode}", retorno+i)
      come_back=mapa_anim.replace(f"{personaje_unicode}{mono_unicode}", f"{b}{b}", retorno_back+i)
      print(come_back)
      time.sleep(0.4)
      os.system("cls")

    pygame.mixer.music.load(song_casa)
    pygame.mixer.music.play(-1)

    print(f"""{Fore.LIGHTWHITE_EX}
*********************************************************************************************************************
*********************************************************************************************************************
*********************************************************************************************************************
*********************************************************************************************************************
***************************************************************************###%##%##*********************************
**************************##%*****************************************#%%#%%#%%%%%%%###%##***************************
*********************##**#%@%#**********************************%###%%%@@@@%@@@@@@@%@%#%%#####***********************
*********************#%@**%%@%**%###%%************************#%%%#%@@%%%@%@@@@@@@@%%%%@%@%%#%%**********************
**********************%%@%#@@#%%#%@%@#*********************##%%%@%%@@@@@%@@@%@@%@@@#%#%%%@@%%@%%%%#******************
**********************%@@@@%@%%%%@%%%#*********************##%%@@@@@%@@###%%#@%%@@@@@@@%@@@@@@%@@%#******************
**************#%@%#****#%%@@@@#%@@%#*****%%##************##%@@@%@@%@@@%%%%%%%@#%%%%%%@%%#%%#@@@@@@%%##***************
***********#%%%#%@%@%@@@%@@@@@@@@%##@@%%##*#**********#%%%@@@@@@@#%##%@@@@@@@@@@@@%%@%@@@@@@@@%@@@%@@%#**************
**************%*#*#%%@%%@@@%@@@@@@@%##*************####%%@%@@@@@%%%@%@@@@@@@@@@@@@@@%@@@@@@@%%#%%@@@@@%@#************
********************%@#%%%@@@@%@%%#%%#%@@@%********##@@@@#%%@@@%@@@@@@@@@@@@@@@@@%%@@@@@@@@@%@@@@%%#@@@@@#***********
*********************%@@@@@@@@@@%%%#%%%%%%%#******%#%%%%@@@@@@@@@@@@%@@@@#@%@*%%%@#%#@@%@@@@@@@@@@@%%@%@*************
*****************%@@@@@#%@@%%%%@%@@%##%%%#******#%%@@%@%@@@@@@%%%#@@@@@**@*@**@#@@**%@@@@@@@@@%@@@@@@%%%%************
**************%@@%%@##*%%%%%%%#@@%@@@###%#%#***#%%%%@@@%@%%%%**%*#*##%@#**%%@*%%**%@*%**@#%@@@@@@@@@@@@%%%***********
************@@%@@#****%%%%#@@%%%@@##@@@@**********###%%*@#%**@%#@#%%*#@#**@@*#%@@#**@@@**#@%@%%%#%%#%%%@@%#**********
***********@##*#******%%@%#%#@%@#%@%*%@@@#****************%%***#**@#*%*@@@#***@*@@*@@#*#@%#@*#%@%%%%%%%**************
**********%*****##%**@%@@#@%#@@*%#@%**#%#@#******%**********@****@*@##**%@*@@**##@@%@@***%%%#@*%%#%%%%%**************
****************%%%%@%%%#@@#*%%#*#@%*****#*#******************@#***@***%*@**@*#**@@@**#%*****##%%%%%%%%%%************
*******%#%%%%%@**%%%@@@%#%@#*@*****##**************@@%@#*************@#@**@@#%@*@@**#**@*#**###%%%%%%%%****%*********
*********%@%#%#%%%%@@@%@@%%#%@%%#***#***#*********#@@@%%%@@#**********@#@**@*@@@@*@#**@**@##*##*%*#%#*%*##*%*********
*******#*######@%@@%@@@%#@%#%@******************#@@@@@@@###%#%%#*******@@**%%*@@%*%%@#*#######%####%*#*#*%%#*********
****************#%%@@@#@%@@%@@@@%%*************@@@@@%@@@#@%%%##%###@#*****@@#@@@***####*##########***%*#%%#%*********                            ¡Vaya!, una casa en medio de esta isla en la que no hay nadie
***********%@@%%%@@@@@%%%##*@*****************@%@@@@@%%@@@%###%#%##%%%%@%***@@@%@@%%#**#########%%%**#%#####*********
******%*%@%@##%@@@%@@@@%%#@@@@%**************%@@@%%#%#%@#%@@%%###%%###%#%#%%%#%%##%@@***########%#%%%#####%@*********                             Quizás haya sido construida por el forastero del que nos habló
*******%@%###@@%%#%@@@%%@%%%@#%#%%*********@@@@@@%%%@#@%%%%@@#%*%#%%%%#@%%@##%%#%%@@@@*#####*%#%#%#%%%@%@#%@*********
****##%%%%%@@@###%@%%@@**%%@@####%%%******@%@@@@@#%@#@@@#%@@@@@@#@%%%%%#%@%%%%%#@@@@@@@###*####%#%%#@@%%%%%%@#*******                             el jefe de la tribu.
*****##%%%@%%%%**%%*#@@#*#%@@@%****##****%#@@@@@@@@%@@@@@%@%%@@@@@@@@%%@#%%%%%#%@@@@@@@#*####%@@%##@@@@*@@%@%********
*****%%#%%%%%%***@%*%@#@@**%@#@%*******@@@@@@@@@@@@#@@**@%%%@%%@@@@@*%@@@@@@@@@@@@@%@@@@#*###*#%@##%@%%%@@%%#%%******                              
****%**@%@%%#%###@*#@@#%%#**@#%%#************@@@@@%%#@**@#%@@@@@@@@@**@@@@@@@@@@*@%@@@@@@#*##%%@%%%##%@%%@@@@#*******
******%####%##*#****%@%*%#**@**#@@***********@@@@@@**@**#@@@@%%@@@@@*#@@@%@@@@@@*@@@@@****###@#%#@@%@%@%@@@@#********                             Vamos a entrar para ver que si hay algo interesante.
******#**#**#****#**#@#**#**@***##***********@##%@%#%##@@@@@@%#%@@@@@@@@@@@@@@@@#@@@@@**#%######@%%%@@%@@%@%%%*******
*******##*#*#***###**@#**#**@**********#@%@@@@@%#%%##@@@@@@@#%%#@%%@#@%%@%@@@@@@%@@@@@**#%#%%%%%@%@%@@@%@@%@%@*******
*******#####*########@###***@**********@@%##%#%@@@@@@@@@@%#%@@@@@%#@%#@#%##@%%%@@%%@@@#%%##%%%%@@####@##@%@@#********
********###**########@###*##@*******#%@@@@@@@@@%@%@@@@%%%@@%@@%#%@%##@##%@%##@#@##@#@#@#@@%#%####%%#@@#@##@@##%******                             Pulsa Enter para entrar en la casa:
*****#######%#%%%#%##@###*##@###**@%%%%%@@%%#%%#%##@%#%%%##%%@@@%##%@@@@@@@@@@@##@@#%@#@#%%%%@@###@%%@@@@@@%@%*******
****%%@%%####*##%%*##@*##*##@%@%#%%%#%%@@@%%#%%@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%@@%%@#@@%%@%#%@********
***#*%%#%@%%#%%%%##*#@#####%@##@@@@%%%##%@@@@@@@@@@@@@@*#@@@@@#@@@@@@@@@%@@@@@%@@@@@@@*#@*@*#@@%#%@%@%@#%#%@%********
*****#%%#@%%#%%%@####@##*###@##**%****#**@**@%@@@@@@@@@@@@@@@@%@@@@@@@@@@@@@@@%@@@%@@@####@#%@%%@%%%%%@#%#%@@********
****%@%#%#@%#%#%%%##%@#####%@##**#****%**@**@%@%@@@%@@@%@@@@@@%@@@%@@%@@@@@@@@%@@@@@@@#%##@%%@@@@#@@#%@@@@@@@@*#*****
****%%@%##@%%%@%#####@%#%##%@##*#%##*#%##@#%@@%%%@@%%@%%@@@@%@#%@@@@@@%@@@@@@@@@@##%@@%%#%@%%@%#@#%@%@%%#@@@@#*******
****%@#*%@@%##@%%#%#%@#%%##@@**#@%%##%%##%%%@%#%%%@%@@%%@%@%@@%%#%%%%@%#@@@@@@#%##%%@@@@@@@#@@#%#%%%#@@*%@#%@********
****#@@%##*####%@%%%#@%%%%%@@###@%%%%%%%%%%#%%%%%%@%@@%@@@@%@%%%%%@@*###%#@@@@#%@##%@@@@%##%#%#%#%#@%@#@@@%#@%%******
****%%##%####@##@@%@%%%%%%%@@####@%@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%@%##%%#@@@%%@%%@%#@@@%%#%%#@%%%#@#%*@%@#%@#%*@*****
****%%%@@@%%%@#@%%#@@@%%@%%@@#*##@#%*%%%@@@@@@@@@@@@@@@@@@@%%#@%%%#%@@@%@@@%%%#@%@@%%##%%%#%%%%%@@%@@@%@%@@*@@*******
*****@#%@@@%@%@##@#%#@%%*#%%@@@%#@%@#@%%@@@@%@@@@@@@@%@%%@%%@%@%%@@###@%@%%#%#%@@#%%%#%%%#%@%@@%@@@%%%@@#@#@@********
****#%%#%#@@@%%@@@#@@####%##%@#%@@%@%%@@@@@@@@@@@@#*@##@%@##%%@@@%@%@@@#@%#%@@@@%%@%%*@@@*%%@##@#@%@%@@@@@@%@#*******
*****@%@@@%@##@%@#%%@@@#%@%@@#%#@@%@@@@@%%@@@@@%##*#####@%%%#%@@#%##%@%%%%@@@@@@@#@@#*#######@@%%###@%%%@@@@@#*******
*****@@%%%#@%%%@%%#@%%#@@##@@%##%#@@@%%%%%%#@@@##%%%#@%%@@@@@@#%%%@%@%%@@%###%@%%@%##@%###@#%%#@%@@@%@@@@@%%@%*******
*****@@@@#@#%%#@@@%%%%%@@#@@%%#%#@@@%@%@@@@%%#@%##%@*%@@##%@%@%%%###%@@##@#@@@@@%%%@@%@%#%@@*%@@@@%%@#@@%@%@%********
****@@@@@@#%@%#@@@@@%@@%@%%@%%%%@@@@@%%%%@%#@%@%@%#%%@@@@%%%@%#%@@@%@%@@@@@@@#@##%@%@@@%@%@@@@@@%@@%@@@@%%%%@%*******
****%@@@@@@@%%##%######%%%@@@@%@@@@@@@@@@@%@@@%@%##@@%@%@##@#%#%@@%@@@%@%@@%#%##%@@%@%@%%%%@@@@@@%@%@@@@@%%@@@*******
*****@@@%%@%%@@%#%##*######################%%%%%%@#@@@@@@@%%#@%%%#@#@#%%@@@#####@#%@*#@#@%%@@@@@@@#%@#@@@%@%@%*%*****
*****@@@@%@@@@@@%%%%%##******************#*##%@@@@%%@@%@#%%%%%@@@%@%@@@@@%@@%%#%@#@@@%@@#@@%@@%@@@@@%@%@@@@@@********
****%@@@@@@%@@@@@@@@@%#######************####%%@@@@@@%@@@@%@@@@@@@@@@@@@@@%@@@@@@@@%@@@@@@#%@@@@@@@@@@@@@@@@@##******
***#%@@@@@%%@@@@@@@@%@@@@%@%%%%#####******************##%@@%%%@@@@@@@@@@@@@%@@%%@@@@@@@%@%@@@@@@@@@@@@@@@@@@@%*******
*****@@@@@@@@@@%%%####%%%%%%@@##**********##%%@@@@@@@%%%@@@@@@@@@@@@@@@%@@@@@@@@@@@@@@@@@@@@@@@@@@@%%%%######********
*****%%%@@@@@@@@@@@@@@@@@@@@%%%%%%%%%%@@@%%@%%%%%@@@@@@@@@@@@@@@@@@@@@@@@%%%###%%%%%@@@@@@@@@@@@@@@@%%%%%####********
**********************************%@@@@@@@@@@@@@@@@@@@@@@@@@@@@%%%%%@%%%%%%%%@%%%@@@@%%%%@@@@@@@%%#%%%@@@@@@%********
*********************************************************************************************************************
*********************************************************************************************************************
*********************************************************************************************************************""")

    input()

    print("""

*********************************************************************************************************************
*********************************************************************************************************************
*********************************************************************************************************************
*********************************************************************************************************************
***************************************************************************###%##%##*********************************
**************************##%*****************************************#%%#%%#%%%%%%%###%##***************************
*********************##**#%@%#**********************************%###%%%@@@@%@@@@@@@%@%#%%#####***********************
*********************#%@**%%@%**%###%%************************#%%%#%@@%%%@%@@@@@@@@%%%%@%@%%#%%**********************
**********************%%@%#@@#%%#%@%@#*********************##%%%@%%@@@@@%@@@%@@%@@@#%#%%%@@%%@%%%%#******************
**********************%@@@@%@%%%%@%%%#*********************##%%@@@@@%@@###%%#@%%@@@@@@@%@@@@@@%@@%#******************
**************#%@%#****#%%@@@@#%@@%#*****%%##************##%@@@%@@%@@@%%%%%%%@#%%%%%%@%%#%%#@@@@@@%%##***************
***********#%%%#%@%@%@@@%@@@@@@@@%##@@%%##*#**********#%%%@@@@@@@#%##%@@@@@@@@@@@@%%@%@@@@@@@@%@@@%@@%#**************                            
**************%*#*#%%@%%@@@%@@@@@@@%##*************####%%@%@@@@@%%%@%@@@@@@@@@@@@@@@%@@@@@@@%%#%%@@@@@%@#************
********************%@#%%%@@@@%@%%#%%#%@@@%********##@@@@#%%@@@%@@@@@@@@@@@@@@@@@%%@@@@@@@@@%@@@@%%#@@@@@#***********
*********************%@@@@@@@@@@%%%#%%%%%%%#******%#%%%%@@@@@@@@@@@@%@@@@#@%@*%%%@#%#@@%@@@@@@@@@@@%%@%@*************                             Hemos entrado en la casa y todo es un desastre, está todo desordenado,
*****************%@@@@@#%@@%%%%@%@@%##%%%#******#%%@@%@%@@@@@@%%%#@@@@@**@*@**@#@@**%@@@@@@@@@%@@@@@@%%%%************
**************%@@%%@##*%%%%%%%#@@%@@@###%#%#***#%%%%@@@%@%%%%**%*#*##%@#**%%@*%%**%@*%**@#%@@@@@@@@@@@@%%%***********                             tirado por el suelo y no hay nada de valor, hay muchas cosas,
************@@%@@#****%%%%#@@%%%@@##@@@@**********###%%*@#%**@%#@#%%*#@#**@@*#%@@#**@@@**#@%@%%%#%%#%%%@@%#**********
***********@##*#******%%@%#%#@%@#%@%*%@@@#****************%%***#**@#*%*@@@#***@*@@*@@#*#@%#@*#%@%%%%%%%**************                             pero podríamos decir que todo lo que hay es basura. 
**********%*****##%**@%@@#@%#@@*%#@%**#%#@#******%**********@****@*@##**%@*@@**##@@%@@***%%%#@*%%#%%%%%**************
****************%%%%@%%%#@@#*%%#*#@%*****#*#******************@#***@***%*@**@*#**@@@**#%*****##%%%%%%%%%%************
*******%#%%%%%@**%%%@@@%#%@#*@*****##**************@@%@#*************@#@**@@#%@*@@**#**@*#**###%%%%%%%%****%*********                             Lo único que parece mantenerse en un estado medio bueno es 
*********%@%#%#%%%%@@@%@@%%#%@%%#***#***#*********#@@@%%%@@#**********@#@**@*@@@@*@#**@**@##*##*%*#%#*%*##*%*********
*******#*######@%@@%@@@%#@%#%@******************#@@@@@@@###%#%%#*******@@**%%*@@%*%%@#*#######%####%*#*#*%%#*********                             un bote con un líquido extraño, tiene una etiqueta que pone... veneno.
****************#%%@@@#@%@@%@@@@%%*************@@@@@%@@@#@%%%##%###@#*****@@#@@@***####*##########***%*#%%#%*********
***********%@@%%%@@@@@%%%##*@*****************@%@@@@@%%@@@%###%#%##%%%%@%***@@@%@@%%#**#########%%%**#%#####*********                             También hay un papel que está en buen estado, y muestra un dibujo,
******%*%@%@##%@@@%@@@@%%#@@@@%**************%@@@%%#%#%@#%@@%%###%%###%#%#%%%#%%##%@@***########%#%%%#####%@*********
*******%@%###@@%%#%@@@%%@%%%@#%#%%*********@@@@@@%%%@#@%%%%@@#%*%#%%%%#@%%@##%%#%%@@@@*#####*%#%#%#%%%@%@#%@*********                             parece que es un mapa.
****##%%%%%@@@###%@%%@@**%%@@####%%%******@%@@@@@#%@#@@@#%@@@@@@#@%%%%%#%@%%%%%#@@@@@@@###*####%#%%#@@%%%%%%@#*******
*****##%%%@%%%%**%%*#@@#*#%@@@%****##****%#@@@@@@@@%@@@@@%@%%@@@@@@@@%%@#%%%%%#%@@@@@@@#*####%@@%##@@@@*@@%@%********
*****%%#%%%%%%***@%*%@#@@**%@#@%*******@@@@@@@@@@@@#@@**@%%%@%%@@@@@*%@@@@@@@@@@@@@%@@@@#*###*#%@##%@%%%@@%%#%%******                             Vamos a ver que podemos hacer en la casa antes de continuar con nuestro
****%**@%@%%#%###@*#@@#%%#**@#%%#************@@@@@%%#@**@#%@@@@@@@@@**@@@@@@@@@@*@%@@@@@@#*##%%@%%%##%@%%@@@@#*******
******%####%##*#****%@%*%#**@**#@@***********@@@@@@**@**#@@@@%%@@@@@*#@@@%@@@@@@*@@@@@****###@#%#@@%@%@%@@@@#********                             viaje.
******#**#**#****#**#@#**#**@***##***********@##%@%#%##@@@@@@%#%@@@@@@@@@@@@@@@@#@@@@@**#%######@%%%@@%@@%@%%%*******
*******##*#*#***###**@#**#**@**********#@%@@@@@%#%%##@@@@@@@#%%#@%%@#@%%@%@@@@@@%@@@@@**#%#%%%%%@%@%@@@%@@%@%@*******
*******#####*########@###***@**********@@%##%#%@@@@@@@@@@%#%@@@@@%#@%#@#%##@%%%@@%%@@@#%%##%%%%@@####@##@%@@#********
********###**########@###*##@*******#%@@@@@@@@@%@%@@@@%%%@@%@@%#%@%##@##%@%##@#@##@#@#@#@@%#%####%%#@@#@##@@##%******                             Pulsa 'm' para abrir el menú:
*****#######%#%%%#%##@###*##@###**@%%%%%@@%%#%%#%##@%#%%%##%%@@@%##%@@@@@@@@@@@##@@#%@#@#%%%%@@###@%%@@@@@@%@%*******
****%%@%%####*##%%*##@*##*##@%@%#%%%#%%@@@%%#%%@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%@@%%@#@@%%@%#%@********
***#*%%#%@%%#%%%%##*#@#####%@##@@@@%%%##%@@@@@@@@@@@@@@*#@@@@@#@@@@@@@@@%@@@@@%@@@@@@@*#@*@*#@@%#%@%@%@#%#%@%********
*****#%%#@%%#%%%@####@##*###@##**%****#**@**@%@@@@@@@@@@@@@@@@%@@@@@@@@@@@@@@@%@@@%@@@####@#%@%%@%%%%%@#%#%@@********
****%@%#%#@%#%#%%%##%@#####%@##**#****%**@**@%@%@@@%@@@%@@@@@@%@@@%@@%@@@@@@@@%@@@@@@@#%##@%%@@@@#@@#%@@@@@@@@*#*****
****%%@%##@%%%@%#####@%#%##%@##*#%##*#%##@#%@@%%%@@%%@%%@@@@%@#%@@@@@@%@@@@@@@@@@##%@@%%#%@%%@%#@#%@%@%%#@@@@#*******
****%@#*%@@%##@%%#%#%@#%%##@@**#@%%##%%##%%%@%#%%%@%@@%%@%@%@@%%#%%%%@%#@@@@@@#%##%%@@@@@@@#@@#%#%%%#@@*%@#%@********
****#@@%##*####%@%%%#@%%%%%@@###@%%%%%%%%%%#%%%%%%@%@@%@@@@%@%%%%%@@*###%#@@@@#%@##%@@@@%##%#%#%#%#@%@#@@@%#@%%******
****%%##%####@##@@%@%%%%%%%@@####@%@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%@%##%%#@@@%%@%%@%#@@@%%#%%#@%%%#@#%*@%@#%@#%*@*****
****%%%@@@%%%@#@%%#@@@%%@%%@@#*##@#%*%%%@@@@@@@@@@@@@@@@@@@%%#@%%%#%@@@%@@@%%%#@%@@%%##%%%#%%%%%@@%@@@%@%@@*@@*******
*****@#%@@@%@%@##@#%#@%%*#%%@@@%#@%@#@%%@@@@%@@@@@@@@%@%%@%%@%@%%@@###@%@%%#%#%@@#%%%#%%%#%@%@@%@@@%%%@@#@#@@********
****#%%#%#@@@%%@@@#@@####%##%@#%@@%@%%@@@@@@@@@@@@#*@##@%@##%%@@@%@%@@@#@%#%@@@@%%@%%*@@@*%%@##@#@%@%@@@@@@%@#*******
*****@%@@@%@##@%@#%%@@@#%@%@@#%#@@%@@@@@%%@@@@@%##*#####@%%%#%@@#%##%@%%%%@@@@@@@#@@#*#######@@%%###@%%%@@@@@#*******
*****@@%%%#@%%%@%%#@%%#@@##@@%##%#@@@%%%%%%#@@@##%%%#@%%@@@@@@#%%%@%@%%@@%###%@%%@%##@%###@#%%#@%@@@%@@@@@%%@%*******
*****@@@@#@#%%#@@@%%%%%@@#@@%%#%#@@@%@%@@@@%%#@%##%@*%@@##%@%@%%%###%@@##@#@@@@@%%%@@%@%#%@@*%@@@@%%@#@@%@%@%********
****@@@@@@#%@%#@@@@@%@@%@%%@%%%%@@@@@%%%%@%#@%@%@%#%%@@@@%%%@%#%@@@%@%@@@@@@@#@##%@%@@@%@%@@@@@@%@@%@@@@%%%%@%*******
****%@@@@@@@%%##%######%%%@@@@%@@@@@@@@@@@%@@@%@%##@@%@%@##@#%#%@@%@@@%@%@@%#%##%@@%@%@%%%%@@@@@@%@%@@@@@%%@@@*******
*****@@@%%@%%@@%#%##*######################%%%%%%@#@@@@@@@%%#@%%%#@#@#%%@@@#####@#%@*#@#@%%@@@@@@@#%@#@@@%@%@%*%*****
*****@@@@%@@@@@@%%%%%##******************#*##%@@@@%%@@%@#%%%%%@@@%@%@@@@@%@@%%#%@#@@@%@@#@@%@@%@@@@@%@%@@@@@@********
****%@@@@@@%@@@@@@@@@%#######************####%%@@@@@@%@@@@%@@@@@@@@@@@@@@@%@@@@@@@@%@@@@@@#%@@@@@@@@@@@@@@@@@##******
***#%@@@@@%%@@@@@@@@%@@@@%@%%%%#####******************##%@@%%%@@@@@@@@@@@@@%@@%%@@@@@@@%@%@@@@@@@@@@@@@@@@@@@%*******
*****@@@@@@@@@@%%%####%%%%%%@@##**********##%%@@@@@@@%%%@@@@@@@@@@@@@@@%@@@@@@@@@@@@@@@@@@@@@@@@@@@%%%%######********
*****%%%@@@@@@@@@@@@@@@@@@@@%%%%%%%%%%@@@%%@%%%%%@@@@@@@@@@@@@@@@@@@@@@@@%%%###%%%%%@@@@@@@@@@@@@@@@%%%%%####********
**********************************%@@@@@@@@@@@@@@@@@@@@@@@@@@@@%%%%%@%%%%%%%%@%%%@@@@%%%%@@@@@@@%%#%%%@@@@@@%********
*********************************************************************************************************************
*********************************************************************************************************************
*********************************************************************************************************************""")



    while casa_v==True:

        if ". Mapa" in objetos:
            opc_menu=input(f"\n{Fore.LIGHTWHITE_EX}Pulsa 'm' y Enter para abrir el menú o pulsa Enter para continuar con el viaje: ")

            if opc_menu!="m":
                casa_v=False
        else:
            opc_menu=input(f"\n{Fore.LIGHTWHITE_EX}Pulsa 'm' y Enter para abrir el menú: ")


        if opc_menu=="m":
          os.system("cls")

          print(casa_menu)
          print(acciones)
            
          print("|  Indica la acción que quieres realizar: ")
          opcion_acc=input("|       --> ")
          

          match opcion_acc:
              case "1":
                  os.system("cls")
                  print(casa_menu)
                  print(coger_intf)
                  opcion_coger=input("       --> ").lower()

                  if opcion_coger=="mapa" or "veneno":
                      if opcion_coger=="mapa":
                          
                          os.system("cls")    
                          print(casa_menu)
                          print("\n\n\nEnhorabuena, has conseguido un mapa, debes de saber que el mapa es un objeto especial y es el único objeto que puedes usarlo independientemente. \nEs decir, no hace falta que lo uses 'con' otro objeto, puedes abrir la opción usar, escribir mapa, y ya podrás optar al él.\n¡Vaya!, parece que hay algo escrito detrás de mapa, veamos que pone.")
                          input("\nPulsa Enter para continuar")
                          os.system("cls")
                          objetos.append(". Mapa")

                          for _ in texto_padre:
                            print(_, end="", flush=True)
                            
                            if _!="\t" and "\n":
                                time.sleep(0.04)

                          input("\n\n\t\t\t\t\t\t\t\t\t\t\t\tPulsa Enter para continuar")



                      elif opcion_coger=="veneno":
                          
                          os.system("cls")    
                          print(casa_menu)
                          print(coger_intf)
                          print("Enhorabuena, se ha añadido el frasco con veneno a tu inventario")
                          objetos.append(". Veneno")

                          input("Pulsa Enter para continuar")


                  else:
                    print("Ahora mismo no hay nada que coger")
                    input("Pulsa Enter para continuar")


              case "2":
                  os.system("cls")
                  print(casa_menu)
                  print(usar_intf)

                  for i in list(objetos):
                      contador_objetos+=1
                      print(contador_objetos, objetos[contador_objetos-1])
                  contador_objetos=0

                  opcion_usar=input("       --> ")

                  if opcion_usar=="mapa" and (". Mapa") in objetos:
                     input("El mapa todavía no se puede usar")

                  elif opcion_usar=="pollo con veneno" and pollo_envenenado==False and (". Veneno") in objetos:
                      print("Enhorabuena, has mezclado el pollo con el veneno y has conseguido un pollo envenenado")

                      objetos.remove(". Pollo")
                      objetos.remove(". Veneno")
                      objetos.append(". Pollo envenenado")
                      pollo_envenenado=True

                      input("Pulsa Enter para continuar")

                  else: 
                    print("Esos objetos no se pueden usar")
                    input("Pulsa Enter para continuar")


              case "3":
                  os.system("cls")
                  print(casa_menu)
                  print(dar_intf)

                  for i in list(objetos):
                      contador_objetos+=1
                      print(contador_objetos, objetos[contador_objetos-1])
                  contador_objetos=0

                  opcion_dar=input("       --> ").lower()
                  print("Esos objetos no se pueden usar")
                  input("Pulsa Enter para continuar")


              case "4":
                  os.system("cls")
                  print(casa_menu)
                  print(inventario_intf)

                  for i in list(objetos):
                      contador_objetos+=1
                      print(contador_objetos, objetos[contador_objetos-1])
                  contador_objetos=0

                  input("\nPulsa Enter para continuar")

              case _:
                  print("Lo siento, está opción no está contemplada")          


        elif opc_menu!="m" and ". Mapa" not in objetos:
            print("Lo siento, está opción no está contemplada")       






    pygame.mixer.music.stop()
    #A partir de aquí empieza el mundo libre 
    while mapa_v==True:
       

      while mapa_obj==True:
        
        #Si da tiempo crear una interfaz para el menú del mapa

        if vuelta1==True:
          direction="N"
          posicion_act=3
          question=5
          posicion[4][0]=True
        
        else:   
          
          mapa_incorrecto=False
          while mapa_incorrecto==False:
            os.system("cls")
            print(mapa_menu)
            mapa_incorrecto=True

            #Pedimos la dirección a la que quiere ir el usuario, para que el flujo del programa se meta en un bloque u en otro
            direction=input(Fore.LIGHTWHITE_EX + "\n\n\t\t\t\t\t\t\t\t¿Hacia que dirección quieres ir, Norte o Sur? (N/S): ")
            direction=direction.upper()


            if direction!="N" and direction!="S":
                print("\n\t\t\t\t\t\t\t\tLo siento, esta opción no es válida, tienes que introducir 'N' o 'S', para ir hacia el Norte o el Sur.")
                mapa_incorrecto=False


            #Le preguntamos al usuario el destino, y le mostramos los posibles destinos a los que puede ir dependiendo de la direeción que haya elegido  

            elif direction=="N" or direction=="S":
                print("\n\t\t\t\t\t\t\t\t¿Hacia donde quieres ir?: ")

                for i in range(6):
                    if direction=="N":
                        if question-1>=posicion[i][1]:
                            continue
                        else:
                            print("\t\t\t\t\t\t\t\t", lugares[i])

                    elif direction=="S":
                        if question-1<=posicion[i][1]:
                            continue
                        else:
                            print("\t\t\t\t\t\t\t\t", lugares[i])


            #Question cambia su valor debido a que se ha elegido un nuevo destino y este destino cambia su valor a True        

                posicion_act=question-1
                question=input("\t\t\t\t\t\t\t\t --> ")
                direction_v=False


            if question in posibles_questions:
                question=int(question)

            else:
                if direction=="N" or direction=="S":
                    input("\n\t\t\t\t\t\t\t\tLo siento, pero esta opción no es válida")
                    question=posicion_act+1
                
            

            #Aseguramos que en cuestion no haya ningún error cuando el ususario introduzca el dato por teclado, y que llo muestre también cuando quiera ir al tesoro sin haber muerto el cocodrilo
            if question==6 and tesoro_v==False:
                input("\n\t\t\t\t\t\t\t\tLo siento, esta zona del mapa está bloqueada por el cocodrilo.")
                question=posicion_act+1
                mapa_incorrecto=False
                    

                    
            #Nos aseguramos con un mensaje de error en caso de que el usuario haya marcado un destino ccontrario a la direccion
            if direction_v==False:

                
                if direction=="N" and posicion_act>question-1:
                    input("\n\t\t\t\t\t\t\t\tEsta opción, no es posible recuerda que has marcado 'ir al Norte'")
                    question=posicion_act+1
                    mapa_incorrecto=False


                elif direction=="S" and posicion_act<question-1:
                    input("\n\t\t\t\t\t\t\t\tEsta opción, no es posible recuerda que has marcado 'ir al Sur'")                                
                    question=posicion_act+1
                    mapa_incorrecto=False

                else:
                    direction_v=True



        posicion[question-1][0]=True


        #Comienza el recorrido del personaje en el mapa 

        #Dirección norte
        if direction=="N":

            if posicion[0][0] and question!=1:
                    
            #Desde la playa hasta la tribu
                
                os.system("cls")
                mapa_anim=mapa.replace(f"{a}", f"{personaje_unicode}", 7)
                come_back=mapa_anim.replace(f"{personaje_unicode}", f"{a}", 6)
                print(come_back)
                time.sleep(1)
                os.system("cls")


                mapa_anim=mapa.replace(f"{c}", f"{personaje_unicode}", 2)
                come_back=mapa_anim.replace(f"{personaje_unicode}", f"{c}", 1)
                print(come_back)
                time.sleep(1)
                os.system("cls")


                mapa_anim=mapa.replace(f"{a}", f"{personaje_unicode}", 6)
                come_back=mapa_anim.replace(f"{personaje_unicode}", f"{a}", 5)
                print(come_back)
                time.sleep(1)
                os.system("cls")
                posicion[0][0]=False


                pygame.mixer.music.load(song_tribu)
                pygame.mixer.music.play(-1)
                while posicion[1][0]==True:
                    
                    os.system("cls")

                    if colmillo_jefe_v==False:
                        print(tribu_menu2)
                        print(acciones)

                    elif colmillo_jefe_v==True:
                        print(tribu_menu4)
                        print(acciones)

                    print("|  Indica la acción que quieres realizar: ")
                    opcion_acc=input("|       --> ")
                        

                    match opcion_acc:
                        case "1":
                            os.system("cls")
                            if colmillo_jefe_v==False:
                                print(tribu_menu2)
                                print(coger_intf)

                            elif colmillo_jefe_v==True:
                                print(tribu_menu4)
                                print(coger_intf)

                            opcion_coger=input("       --> ")
                            print("Ahora mismo no hay nada que coger")
                            input("Pulsa Enter para continuar")


                        case "2":
                            os.system("cls")
                            if colmillo_jefe_v==False:
                                print(tribu_menu2)
                                print(usar_intf)

                            elif colmillo_jefe_v==True:
                                print(tribu_menu4)
                                print(usar_intf)

                            for i in list(objetos):
                                contador_objetos+=1
                                print(contador_objetos, objetos[contador_objetos-1])
                            contador_objetos=0

                            opcion_usar=input("       --> ").lower()

                            if opcion_usar=="pollo con veneno" and pollo_envenenado==False and (". Veneno") in objetos and tesoro_v==False:
                                print("Enhorabuena, has mezclado el pollo con el veneno y has conseguido un pollo envenenado")

                                objetos.remove(". Pollo")
                                objetos.remove(". Veneno")
                                objetos.append(". Pollo envenenado")
                                pollo_envenenado=True

                                input("Pulsa Enter para continuar")

                            if opcion_usar=="mapa":
                                vuelta1=False
                                break
                                   

                            else:
                                print("Esos objetos no se pueden usar")
                                input("Pulsa Enter para continuar")


                        case "3":
                            os.system("cls")
                            if colmillo_jefe_v==False:
                                print(tribu_menu2)
                                print(dar_intf)

                            elif colmillo_jefe_v==True:
                                print(tribu_menu4)
                                print(dar_intf)

                            for i in list(objetos):
                                contador_objetos+=1
                                print(contador_objetos, objetos[contador_objetos-1])
                            contador_objetos=0

                            opcion_dar=input("       --> ").lower()

                            if ". Colmillo" in objetos and opcion_dar=="colmillo a jefe":
                                os.system("cls")
                                print(tribu_menu3)
                                objetos.remove(". Colmillo")
                                objetos.append(". Llave")
                                colmillo_jefe_v=True

                                input("Pulsa Enter para continuar")

                            else:
                                print("No puedes dar este objeto")
                                input("Pulsa Enter para continuar")                            



                        case "4":
                            os.system("cls")
                            if colmillo_jefe_v==False:
                                print(tribu_menu2)
                                print(inventario_intf)

                            elif colmillo_jefe_v==True:
                                print(tribu_menu4)
                                print(inventario_intf)

                            for i in list(objetos):
                                contador_objetos+=1
                                print(contador_objetos, objetos[contador_objetos-1])
                            contador_objetos=0

                            input("\nPulsa Enter para continuar")

                        case _:
                            print("Lo siento, está opción no está contemplada") 



            pygame.mixer.music.stop()

            for i in posicion:
                if (i[1]>1 and i[0]==True) and (posicion_act<2):

                    
                    
                #Desde la tribu hasta la selva
                    
                    os.system("cls")
                    mapa_anim=mapa.replace(f"{d}", f"{personaje_unicode}", 4)
                    come_back=mapa_anim.replace(f"{personaje_unicode}", f"{d}", 3)
                    print(come_back)
                    time.sleep(1)
                    os.system("cls")


                    mapa_anim=mapa.replace(f"{a}", f"{personaje_unicode}", 5)
                    come_back=mapa_anim.replace(f"{personaje_unicode}", f"{a}", 4)
                    print(come_back)
                    time.sleep(1)
                    os.system("cls")


                    mapa_anim=mapa.replace(f"{a}", f"{personaje_unicode}", 4)
                    come_back=mapa_anim.replace(f"{personaje_unicode}", f"{a}", 3)
                    print(come_back)
                    time.sleep(1)
                    os.system("cls")
                    posicion[1][0]=False
                    
                    pygame.mixer.music.load(song_selva)
                    pygame.mixer.music.play(-1)

                    while posicion[2][0]==True:


                        print(selva_menu)
                        print(acciones)
                          
                        print("|  Indica la acción que quieres realizar: ")
                        opcion_acc=input("|       --> ")
                        

                        match opcion_acc:
                            case "1":
                                os.system("cls")
                                print(selva_menu)
                                print(coger_intf)
                                opcion_coger=input("       --> ")
                                print("Ahora mismo no hay nada que coger")
                                input("Pulsa Enter para continuar")


                            case "2":
                                os.system("cls")
                                print(selva_menu)
                                print(usar_intf)

                                for i in list(objetos):
                                    contador_objetos+=1
                                    print(contador_objetos, objetos[contador_objetos-1])
                                contador_objetos=0

                                opcion_usar=input("       --> ").lower()

                                if opcion_usar=="pollo con veneno" and pollo_envenenado==False and (". Veneno") in objetos:
                                   print("Enhorabuena, has mezclado el pollo con el veneno y has conseguido un pollo envenenado")

                                   objetos.remove(". Pollo")
                                   objetos.remove(". Veneno")
                                   objetos.append(". Pollo envenenado")
                                   pollo_envenenado=True

                                   input("Pulsa Enter para continuar")

                                if opcion_usar=="mapa":
                                   vuelta1=False
                                   break
                                   

                                else:
                                  print("Esos objetos no se pueden usar")
                                  input("Pulsa Enter para continuar")


                            case "3":
                                os.system("cls")
                                print(selva_menu)
                                print(dar_intf)

                                for i in list(objetos):
                                    contador_objetos+=1
                                    print(contador_objetos, objetos[contador_objetos-1])
                                contador_objetos=0

                                opcion_dar=input("       --> ").lower()
                                print("No puedes dar este objeto")
                                input("Pulsa Enter para continuar")


                            case "4":
                                os.system("cls")
                                print(selva_menu)
                                print(inventario_intf)

                                for i in list(objetos):
                                    contador_objetos+=1
                                    print(contador_objetos, objetos[contador_objetos-1])
                                contador_objetos=0

                                input("\nPulsa Enter para continuar")

                            case _:
                              print("Lo siento, está opción no está contemplada")   


            pygame.mixer.music.stop()           
            for i in posicion:
                if (i[1]>2 and i[0]==True) and (posicion_act<3):

                #Desde la selva a casa abandonada
                    os.system("cls")                    
                    retorno=1
                    retorno_back=0

                    for i in range(9):
                        mapa_anim=mapa.replace(f"{b}{b}", f"{personaje_unicode}{mono_unicode}", retorno+i)
                        come_back=mapa_anim.replace(f"{personaje_unicode}{mono_unicode}", f"{b}{b}", retorno_back+i)
                        print(come_back)
                        time.sleep(0.4)
                        os.system("cls")
                        posicion[2][0]=False
                    
                    pygame.mixer.music.load(song_casa)
                    pygame.mixer.music.play(-1)

                    while posicion[3][0]==True:

                        print(casa_menu)
                        print(acciones)
                          
                        print("|  Indica la acción que quieres realizar: ")
                        opcion_acc=input("|       --> ")
                        

                        match opcion_acc:
                            case "1":
                                os.system("cls")
                                print(casa_menu)
                                print(coger_intf)
                                opcion_coger=input("       --> ").lower()

                                if opcion_coger=="veneno" and veneno_v==False:
                                    objetos.append(". Veneno")
                                    print("¡Estupendo!, has cogido el frasco lleno de veneno")
                                    veneno_v=True
                                    input("Pulsa Enter para volver al menú: ")

                                else:
                                    print("Ahora mismo no hay nada que coger")
                                    input("Pulsa Enter para continuar")


                            case "2":
                                os.system("cls")
                                print(casa_menu)
                                print(usar_intf)

                                for i in list(objetos):
                                    contador_objetos+=1
                                    print(contador_objetos, objetos[contador_objetos-1])
                                contador_objetos=0

                                opcion_usar=input("       --> ").lower()

                                if opcion_usar=="pollo con veneno" and pollo_envenenado==False and (". Veneno") in objetos:
                                   print("Enhorabuena, has mezclado el pollo con el veneno y has conseguido un pollo envenenado")

                                   objetos.remove(". Pollo")
                                   objetos.remove(". Veneno")
                                   objetos.append(". Pollo envenenado")
                                   pollo_envenenado=True

                                   input("Pulsa Enter para volver al menú: ")

                                elif opcion_usar=="mapa":
                                   break
                                   

                                else:
                                  print("Esos objetos no se pueden usar")
                                  input("Pulsa Enter para continuar")


                            case "3":
                                os.system("cls")
                                print(casa_menu)
                                print(dar_intf)

                                for i in list(objetos):
                                    contador_objetos+=1
                                    print(contador_objetos, objetos[contador_objetos-1])
                                contador_objetos=0

                                opcion_dar=input("       --> ").lower()
                                print("No puedes dar este objeto")
                                input("Pulsa Enter para continuar")


                            case "4":
                                os.system("cls")
                                print(casa_menu)
                                print(inventario_intf)

                                for i in list(objetos):
                                    contador_objetos+=1
                                    print(contador_objetos, objetos[contador_objetos-1])
                                contador_objetos=0

                                input("\nPulsa Enter para continuar")

                            case _:
                              print("Lo siento, está opción no está contemplada")  


            pygame.mixer.music.stop()
            for i in posicion:
                if (i[1]>3 and i[0]==True) and (posicion_act<4):

            #Desde la casa abandonada al pantano con cocodrilos
                    
                    os.system("cls")
                    mapa_anim=mapa.replace(f"{d}", f"{personaje_unicode}", 3)
                    come_back=mapa_anim.replace(f"{personaje_unicode}", f"{d}", 2)
                    print(come_back)
                    time.sleep(1)
                    os.system("cls")


                    mapa_anim=mapa.replace(f"{d}", f"{personaje_unicode}", 2)
                    come_back=mapa_anim.replace(f"{personaje_unicode}", f"{d}", 1)
                    print(come_back)
                    time.sleep(1)
                    os.system("cls")


                    come_back=mapa.replace(f"{d}", f"{personaje_unicode}", 1)
                    print(come_back)
                    time.sleep(1)
                    os.system("cls")
                    posicion[3][0]=False
                    

                    pygame.mixer.music.load(song_pantano)
                    pygame.mixer.music.play(-1)

                    while posicion[4][0]==True:

                        os.system("cls")


                        if cocodrilo_muerto==False:
                            print(pantano)
                            print(acciones)

                        elif cocodrilo_muerto==True and (". Colmillo") not in objetos:
                            print(pantano2)
                            print(acciones)

                        elif cocodrilo_muerto==True and (". Colmillo") in objetos:
                            print(pantano3)
                            print(acciones)

                            
                        print("|  Indica la acción que quieres realizar: ")
                        opcion_acc=input("|       --> ")
                            

                        match opcion_acc:
                            case "1":
                                os.system("cls")

                                if cocodrilo_muerto==False:
                                    print(pantano)
                                    print(coger_intf)

                                elif cocodrilo_muerto==True and (". Colmillo") not in objetos:
                                    print(pantano2)
                                    print(coger_intf)

                                elif cocodrilo_muerto==True and (". Colmillo") in objetos:
                                    print(pantano3)
                                    print(coger_intf)

                                opcion_coger=input("       --> ").lower()

                                if opcion_coger=="colmillo" and (". Colmillo") not in objetos:
                                    print("¡Genial!, has cogido el colmillo del cocodrilo gigante.\nYa está incluido en tu inventario.")

                                    objetos.append(". Colmillo")

                                    input("Pulsa Enter para continuar")
                                    
                                else:
                                    print("No puedes coger ese objeto")
                                    input("Pulsa Enter para continuar")


                            case "2":
                                os.system("cls")
                                if cocodrilo_muerto==False:
                                    print(pantano)
                                    print(usar_intf)

                                elif cocodrilo_muerto==True and (". Colmillo") not in objetos:
                                    print(pantano2)
                                    print(usar_intf)

                                elif cocodrilo_muerto==True and (". Colmillo") in objetos:
                                    print(pantano3)
                                    print(usar_intf)


                                for i in list(objetos):
                                    contador_objetos+=1
                                    print(contador_objetos, objetos[contador_objetos-1])
                                contador_objetos=0

                                opcion_usar=input("       --> ").lower()

                                if opcion_usar=="pollo con veneno" and pollo_envenenado==False and (". Veneno") in objetos:
                                    print("Enhorabuena, has mezclado el pollo con el veneno y has conseguido un pollo envenenado")

                                    objetos.remove(". Pollo")
                                    objetos.remove(". Veneno")
                                    objetos.append(". Pollo envenenado")
                                    pollo_envenenado=True

                                    input("Pulsa Enter para continuar")

                                elif opcion_usar=="mapa":
                                    vuelta1=False
                                    break
                                    

                                else:
                                    print("Esos objetos no se pueden usar")
                                    input("Pulsa Enter para continuar")


                            case "3":
                                os.system("cls")
                                if cocodrilo_muerto==False:
                                    print(pantano)
                                    print(dar_intf)

                                elif cocodrilo_muerto==True and (". Colmillo") not in objetos:
                                    print(pantano2)
                                    print(dar_intf)

                                elif cocodrilo_muerto==True and (". Colmillo") in objetos:
                                    print(pantano3)
                                    print(dar_intf)


                                for i in list(objetos):
                                    contador_objetos+=1
                                    print(contador_objetos, objetos[contador_objetos-1])
                                contador_objetos=0

                                opcion_dar=input("       --> ").lower()

                                if ". Pollo envenenado" in objetos and opcion_dar=="pollo envenenado a cocodrilo":
                                    print("Enhorabuena, has conseguido matar al cocodrilo, esto ha dejado la vía libre.\nHas desbloqueado el último punto de la isla, 'el tesoro', ahora puedes viajar haciia allí.")
                                    objetos.remove(". Pollo envenenado")
                                    tesoro_v=True
                                    cocodrilo_muerto=True


                                    input("Pulsa Enter para continuar")

                                else:
                                    print("No puedes dar este objeto")
                                    input("Pulsa Enter para continuar")


                            case "4":
                                os.system("cls")
                                if cocodrilo_muerto==False:
                                    print(pantano)
                                    print(inventario_intf)

                                elif cocodrilo_muerto==True and (". Colmillo") not in objetos:
                                    print(pantano2)
                                    print(inventario_intf)

                                elif cocodrilo_muerto==True and (". Colmillo") in objetos:
                                    print(pantano3)
                                    print(inventario_intf)


                                for i in list(objetos):
                                    contador_objetos+=1
                                    print(contador_objetos, objetos[contador_objetos-1])
                                contador_objetos=0

                                input("\nPulsa Enter para continuar")

                            case _:
                                print("Lo siento, está opción no está contemplada") 
                                    

            pygame.mixer.music.stop()            
            for i in posicion:
                if (i[1]==5 and i[0]==True) and (posicion_act<5) and tesoro_v==True:

                        
                #Desde el pantano hasta el cofre del tesoro
                    
                    os.system("cls")
                    mapa_anim=mapa.replace(f"{a}", f"{personaje_unicode}", 3)
                    come_back=mapa_anim.replace(f"{personaje_unicode}", f"{a}", 2)
                    print(come_back)
                    time.sleep(1)
                    os.system("cls")


                    come_back=mapa.replace(f"{c}", f"{personaje_unicode}", 1)
                    print(come_back)
                    time.sleep(1)
                    os.system("cls")


                    mapa_anim=mapa.replace(f"{a}", f"{personaje_unicode}", 2)
                    come_back=mapa_anim.replace(f"{personaje_unicode}", f"{a}", 1)
                    print(come_back)
                    time.sleep(1)
                    os.system("cls")


                    come_back=mapa.replace(f"{a}", f"{personaje_unicode}", 1)
                    print(come_back)
                    time.sleep(1)
                    os.system("cls")


                    print(mapa)
                    time.sleep(1)
                    os.system("cls")
                    posicion[4][0]=False
                    

                    
                    while tesoro_v==True:

                        os.system("cls")

                        print(cofre)
                        print(acciones)
                          
                        print("|  Indica la acción que quieres realizar: ")
                        opcion_acc=input("|       --> ")
                        

                        match opcion_acc:
                            case "1":
                                os.system("cls")
                                print(cofre)
                                print(coger_intf)
                                opcion_coger=input("       --> ")
                                print("Ahora mismo no hay nada que coger")
                                input("Pulsa Enter para continuar")


                            case "2":
                                os.system("cls")
                                print(cofre)
                                print(usar_intf)

                                for i in list(objetos):
                                    contador_objetos+=1
                                    print(contador_objetos, objetos[contador_objetos-1])
                                contador_objetos=0

                                opcion_usar=input("       --> ").lower()

                                if (opcion_usar=="llave con cofre" or opcion_usar=="llave con tesoro") and (". Llave") in objetos:
                                    os.system("cls")
                                    pygame.mixer.music.load(song_final)
                                    pygame.mixer.music.play()


                                    print(cofre_open)

                                    input()

                                    pygame.mixer.music.stop()
                                    sys.exit()
                                    

                                elif opcion_usar=="mapa":
                                    vuelta1=False
                                    break

                                else:
                                    print("Esos objetos no se pueden usar")
                                    input("Pulsa Enter para continuar")


                            case "3":
                                os.system("cls")
                                print(cofre)
                                print(dar_intf)

                                for i in list(objetos):
                                    contador_objetos+=1
                                    print(contador_objetos, objetos[contador_objetos-1])
                                contador_objetos=0

                                opcion_dar=input("       --> ").lower()
                                print("No puedes dar este objeto")
                                input("Pulsa Enter para continuar")


                            case "4":
                                os.system("cls")
                                print(cofre)
                                print(inventario_intf)

                                for i in list(objetos):
                                    contador_objetos+=1
                                    print(contador_objetos, objetos[contador_objetos-1])
                                contador_objetos=0

                                input("\nPulsa Enter para continuar")

                            case _:
                              print("Lo siento, está opción no está contemplada")   










        if direction=="S":

            if posicion[5][0] and question!=6:


                #Desde el tesoro hasta el pantano de cocodrilos

                os.system("cls")
                mapa_anim=mapa
                come_back=mapa_anim.replace(f"{a}", f"{personaje_unicode}", 1)
                print(come_back)
                time.sleep(1)
                os.system("cls")            

                mapa_anim=mapa.replace(f"{a}", f"{personaje_unicode}", 2)
                come_back=mapa_anim.replace(f"{personaje_unicode}", f"{a}", 1)
                print(come_back)
                time.sleep(1)
                os.system("cls")

                come_back=mapa.replace(f"{c}", f"{personaje_unicode}", 1)
                print(come_back)
                time.sleep(1)
                os.system("cls")

                mapa_anim=mapa.replace(f"{a}", f"{personaje_unicode}", 3)
                come_back=mapa_anim.replace(f"{personaje_unicode}", f"{a}", 2)
                print(come_back)
                time.sleep(1)
                os.system("cls")
                posicion[5][0]=False

                pygame.mixer.music.load(song_pantano)
                pygame.mixer.music.play(-1)

                while posicion[4][0]==True:

                    print(pantano)
                    print(acciones)
                          
                    print("|  Indica la acción que quieres realizar: ")
                    opcion_acc=input("|       --> ")
                        

                while posicion[4][0]==True:
                        
                        os.system("cls")


                        if cocodrilo_muerto==True and (". Colmillo") not in objetos:
                            print(pantano2)
                            print(acciones)

                        elif cocodrilo_muerto==True and (". Colmillo") in objetos:
                            print(pantano3)
                            print(acciones)

                            
                        print("|  Indica la acción que quieres realizar: ")
                        opcion_acc=input("|       --> ")
                            

                        match opcion_acc:
                            case "1":
                                os.system("cls")

                                if cocodrilo_muerto==True and (". Colmillo") not in objetos:
                                    print(pantano2)
                                    print(coger_intf)

                                elif cocodrilo_muerto==True and (". Colmillo") in objetos:
                                    print(pantano3)
                                    print(coger_intf)

                                opcion_coger=input("       --> ").lower()

                                if opcion_coger=="colmillo" and (". Colmillo") not in objetos:
                                    print("¡Genial!, has cogido el colmillo del cocodrilo gigante.\nYa está incluido en tu inventario.")

                                    objetos.append(". Colmillo")

                                    input("Pulsa Enter para continuar")
                                    
                                else:
                                    print("No puedes coger ese objeto")
                                    input("Pulsa Enter para continuar")


                            case "2":
                                os.system("cls")

                                if cocodrilo_muerto==True and (". Colmillo") not in objetos:
                                    print(pantano2)
                                    print(usar_intf)

                                elif cocodrilo_muerto==True and (". Colmillo") in objetos:
                                    print(pantano3)
                                    print(usar_intf)


                                for i in list(objetos):
                                    contador_objetos+=1
                                    print(contador_objetos, objetos[contador_objetos-1])
                                contador_objetos=0

                                opcion_usar=input("       --> ").lower()

                                if opcion_usar=="mapa":
                                    vuelta1=False
                                    break

                                else:
                                    print("Esos objetos no se pueden usar")
                                    input("Pulsa Enter para continuar")


                            case "3":
                                os.system("cls")

                                if cocodrilo_muerto==True and (". Colmillo") not in objetos:
                                    print(pantano2)
                                    print(dar_intf)

                                elif cocodrilo_muerto==True and (". Colmillo") in objetos:
                                    print(pantano3)
                                    print(dar_intf)


                                for i in list(objetos):
                                    contador_objetos+=1
                                    print(contador_objetos, objetos[contador_objetos-1])
                                contador_objetos=0

                                opcion_dar=input("       --> ").lower()
                                print("No puedes dar este objeto")
                                input("Pulsa Enter para continuar")


                            case "4":
                                os.system("cls")

                                if cocodrilo_muerto==True and (". Colmillo") not in objetos:
                                    print(pantano2)
                                    print(inventario_intf)

                                elif cocodrilo_muerto==True and (". Colmillo") in objetos:
                                    print(pantano3)
                                    print(inventario_intf)


                                for i in list(objetos):
                                    contador_objetos+=1
                                    print(contador_objetos, objetos[contador_objetos-1])
                                contador_objetos=0

                                input("\nPulsa Enter para continuar")

                            case _:
                                print("Lo siento, está opción no está contemplada") 

                

            pygame.mixer.music.stop()
            for i in posicion:
                if (i[1]<4 and i[0]==True) and (posicion_act>3): 
           

                #Desde el pantano de cocodrilos hasta la casa abandonada
                    
                    os.system("cls")
                    come_back=mapa.replace(f"{d}", f"{personaje_unicode}", 1)
                    print(come_back)
                    time.sleep(1)
                    os.system("cls")

                    mapa_anim=mapa.replace(f"{d}", f"{personaje_unicode}", 2)
                    come_back=mapa_anim.replace(f"{personaje_unicode}", f"{d}", 1)
                    print(come_back)
                    time.sleep(1)
                    os.system("cls")


                    mapa_anim=mapa.replace(f"{d}", f"{personaje_unicode}", 3)
                    come_back=mapa_anim.replace(f"{personaje_unicode}", f"{d}", 2)
                    print(come_back)
                    time.sleep(1)
                    os.system("cls")
                    posicion[4][0]=False

                    pygame.mixer.music.load(song_casa)
                    pygame.mixer.music.play(-1)

                    while posicion[3][0]==True:
                        
                        print(casa_menu)
                        print(acciones)
                          
                        print("|  Indica la acción que quieres realizar: ")
                        opcion_acc=input("|       --> ")
                        

                        match opcion_acc:
                            case "1":
                                os.system("cls")
                                print(casa_menu)
                                print(coger_intf)
                                opcion_coger=input("       --> ").lower()

                                if opcion_coger=="veneno" and veneno_v==False:
                                    objetos.append(". Veneno")
                                    print("¡Estupendo!, has cogido el frasco lleno de veneno")
                                    veneno_v=True
                                    input("Pulsa Enter para volver al menú: ")

                                else:
                                    print("Ahora mismo no hay nada que coger")
                                    input("Pulsa Enter para continuar")


                            case "2":
                                os.system("cls")
                                print(casa_menu)
                                print(usar_intf)

                                for i in list(objetos):
                                    contador_objetos+=1
                                    print(contador_objetos, objetos[contador_objetos-1])
                                contador_objetos=0

                                opcion_usar=input("       --> ").lower()

                                if opcion_usar=="pollo con veneno" and pollo_envenenado==False and (". Veneno") in objetos:
                                   print("Enhorabuena, has mezclado el pollo con el veneno y has conseguido un pollo envenenado")

                                   objetos.remove(". Pollo")
                                   objetos.remove(". Veneno")
                                   objetos.append(". Pollo envenenado")
                                   pollo_envenenado=True

                                   input("Pulsa Enter para continuar")

                                if opcion_usar=="mapa":
                                   vuelta1=False
                                   break
                                   

                                else:
                                  print("Esos objetos no se pueden usar")
                                  input("Pulsa Enter para continuar")


                            case "3":
                                os.system("cls")
                                print(casa_menu)
                                print(dar_intf)

                                for i in list(objetos):
                                    contador_objetos+=1
                                    print(contador_objetos, objetos[contador_objetos-1])
                                contador_objetos=0

                                opcion_dar=input("       --> ").lower()
                                print("No puedes dar este objeto")
                                input("Pulsa Enter para continuar")


                            case "4":
                                os.system("cls")
                                print(casa_menu)
                                print(inventario_intf)

                                for i in list(objetos):
                                    contador_objetos+=1
                                    print(contador_objetos, objetos[contador_objetos-1])
                                contador_objetos=0

                                input("\nPulsa Enter para continuar")

                            case _:
                              print("Lo siento, está opción no está contemplada") 
                    


                    

            pygame.mixer.music.stop()            
            for i in posicion:
                if (i[1]<3 and i[0]==True) and (posicion_act>2):



                #Desde la casa abandonada hasta la selva
                    
                    os.system("cls")
                    retorno=1
                    retorno_back=0
                    for i in range(8,-1,-1):
                        mapa_anim=mapa.replace(f"{b}{b}", f"{mono_unicode}{personaje_unicode}", retorno+i)
                        come_back=mapa_anim.replace(f"{mono_unicode}{personaje_unicode}", f"{b}{b}", retorno_back+i)
                        print(come_back)
                        time.sleep(0.4)
                        os.system("cls")
                        posicion[3][0]=False

                    pygame.mixer.music.load(song_selva)
                    pygame.mixer.music.play(-1)

                    while posicion[2][0]==True:

                        print(selva_menu)
                        print(acciones)
                          
                        print("|  Indica la acción que quieres realizar: ")
                        opcion_acc=input("|       --> ")
                        

                        match opcion_acc:
                            case "1":
                                os.system("cls")
                                print(selva_menu)
                                print(coger_intf)
                                opcion_coger=input("       --> ")
                                print("Ahora mismo no hay nada que coger")
                                input("Pulsa Enter para continuar")


                            case "2":
                                os.system("cls")
                                print(selva_menu)
                                print(usar_intf)

                                for i in list(objetos):
                                    contador_objetos+=1
                                    print(contador_objetos, objetos[contador_objetos-1])
                                contador_objetos=0

                                opcion_usar=input("       --> ").lower()

                                if opcion_usar=="pollo con veneno" and pollo_envenenado==False and (". Veneno") in objetos:
                                   print("Enhorabuena, has mezclado el pollo con el veneno y has conseguido un pollo envenenado")

                                   objetos.remove(". Pollo")
                                   objetos.remove(". Veneno")
                                   objetos.append(". Pollo envenenado")
                                   pollo_envenenado=True

                                   input("Pulsa Enter para continuar")

                                if opcion_usar=="mapa":
                                   vuelta1=False
                                   break
                                   

                                else:
                                  print("Esos objetos no se pueden usar")
                                  input("Pulsa Enter para continuar")


                            case "3":
                                os.system("cls")
                                print(selva_menu)
                                print(dar_intf)

                                for i in list(objetos):
                                    contador_objetos+=1
                                    print(contador_objetos, objetos[contador_objetos-1])
                                contador_objetos=0

                                opcion_dar=input("       --> ").lower()
                                print("No puedes dar este objeto")
                                input("Pulsa Enter para continuar")


                            case "4":
                                os.system("cls")
                                print(selva_menu)
                                print(inventario_intf)

                                for i in list(objetos):
                                    contador_objetos+=1
                                    print(contador_objetos, objetos[contador_objetos-1])
                                contador_objetos=0

                                input("\nPulsa Enter para continuar")

                            case _:
                              print("Lo siento, está opción no está contemplada") 


            pygame.mixer.music.stop()
            for i in posicion:
                if (i[1]<2 and i[0]==True) and (posicion_act>1):



                    #Desde la selva hasta la tribu

                    os.system("cls")
                    mapa_anim=mapa.replace(f"{a}", f"{personaje_unicode}", 4)
                    come_back=mapa_anim.replace(f"{personaje_unicode}", f"{a}", 3)
                    print(come_back)
                    time.sleep(1)
                    os.system("cls")


                    mapa_anim=mapa.replace(f"{a}", f"{personaje_unicode}", 5)
                    come_back=mapa_anim.replace(f"{personaje_unicode}", f"{a}", 4)
                    print(come_back)
                    time.sleep(1)
                    os.system("cls")


                    mapa_anim=mapa.replace(f"{d}", f"{personaje_unicode}", 4)
                    come_back=mapa_anim.replace(f"{personaje_unicode}", f"{d}", 3)
                    print(come_back)
                    time.sleep(1)
                    os.system("cls")
                    posicion[2][0]=False

                    pygame.mixer.music.load(song_tribu)
                    pygame.mixer.music.play(-1)

                    while posicion[1][0]==True:

                        os.system("cls")

                        if colmillo_jefe_v==False:
                            print(tribu_menu2)
                            print(acciones)

                        elif colmillo_jefe_v==True:
                            print(tribu_menu4)
                            print(acciones)

                        print("|  Indica la acción que quieres realizar: ")
                        opcion_acc=input("|       --> ")
                            

                        match opcion_acc:
                            case "1":
                                os.system("cls")
                                if colmillo_jefe_v==False:
                                    print(tribu_menu2)
                                    print(coger_intf)

                                elif colmillo_jefe_v==True:
                                    print(tribu_menu4)
                                    print(coger_intf)

                                opcion_coger=input("       --> ")
                                print("Ahora mismo no hay nada que coger")
                                input("Pulsa Enter para continuar")


                            case "2":
                                os.system("cls")
                                if colmillo_jefe_v==False:
                                    print(tribu_menu2)
                                    print(usar_intf)

                                elif colmillo_jefe_v==True:
                                    print(tribu_menu4)
                                    print(usar_intf)

                                for i in list(objetos):
                                    contador_objetos+=1
                                    print(contador_objetos, objetos[contador_objetos-1])
                                contador_objetos=0

                                opcion_usar=input("       --> ").lower()

                                if opcion_usar=="pollo con veneno" and pollo_envenenado==False and (". Veneno") in objetos and tesoro_v==False:
                                    print("Enhorabuena, has mezclado el pollo con el veneno y has conseguido un pollo envenenado")

                                    objetos.remove(". Pollo")
                                    objetos.remove(". Veneno")
                                    objetos.append(". Pollo envenenado")
                                    pollo_envenenado=True

                                    input("Pulsa Enter para continuar")

                                if opcion_usar=="mapa":
                                    vuelta1=False
                                    break
                                    

                                else:
                                    print("Esos objetos no se pueden usar")
                                    input("Pulsa Enter para continuar")


                            case "3":
                                os.system("cls")
                                if colmillo_jefe_v==False:
                                    print(tribu_menu2)
                                    print(dar_intf)

                                elif colmillo_jefe_v==True:
                                    print(tribu_menu4)
                                    print(dar_intf)

                                for i in list(objetos):
                                    contador_objetos+=1
                                    print(contador_objetos, objetos[contador_objetos-1])
                                contador_objetos=0

                                opcion_dar=input("       --> ").lower()

                                if ". Colmillo" in objetos and opcion_dar=="colmillo a jefe":
                                    os.system("cls")
                                    print(tribu_menu3)
                                    objetos.remove(". Colmillo")
                                    objetos.append(". Llave")
                                    colmillo_jefe_v=True


                                    input("Pulsa Enter para continuar")

                                else:
                                    print("No puedes dar este objeto")
                                    input("Pulsa Enter para continuar")                            



                            case "4":
                                os.system("cls")
                                if colmillo_jefe_v==False:
                                    print(tribu_menu2)
                                    print(inventario_intf)

                                elif colmillo_jefe_v==True:
                                    print(tribu_menu4)
                                    print(inventario_intf)

                                for i in list(objetos):
                                    contador_objetos+=1
                                    print(contador_objetos, objetos[contador_objetos-1])
                                contador_objetos=0

                                input("\nPulsa Enter para continuar")

                            case _:
                                print("Lo siento, está opción no está contemplada") 



            pygame.mixer.music.stop()
            for i in posicion:
                if (i[1]==0 and i[0]==True) and (posicion_act>0):    



                    #Desde la tribu hasta la playa

                    os.system("cls")
                    mapa_anim=mapa.replace(f"{a}", f"{personaje_unicode}", 6)
                    come_back=mapa_anim.replace(f"{personaje_unicode}", f"{a}", 5)
                    print(come_back)
                    time.sleep(1)
                    os.system("cls")

                    mapa_anim=mapa.replace(f"{c}", f"{personaje_unicode}", 2)
                    come_back=mapa_anim.replace(f"{personaje_unicode}", f"{c}", 1)
                    print(come_back)
                    time.sleep(1)
                    os.system("cls")


                    mapa_anim=mapa.replace(f"{a}", f"{personaje_unicode}", 7)
                    come_back=mapa_anim.replace(f"{personaje_unicode}", f"{a}", 6)
                    print(come_back)
                    time.sleep(1)
                    os.system("cls")


                    print(mapa)
                    time.sleep(1)
                    os.system("cls")
                    posicion[1][0]=False

                    pygame.mixer.music.load(song_playa)
                    pygame.mixer.music.play(-1)

                    while posicion[0][0]==True:

                        print(playa)
                        print(acciones)
                          
                        print("|  Indica la acción que quieres realizar: ")
                        opcion_acc=input("|       --> ")
                        

                        match opcion_acc:
                            case "1":
                                os.system("cls")
                                print(playa)
                                print(coger_intf)
                                opcion_coger=input("       --> ")
                                print("Ahora mismo no hay nada que coger")
                                input("Pulsa Enter para continuar")


                            case "2":
                                os.system("cls")
                                print(playa)
                                print(usar_intf)

                                for i in list(objetos):
                                    contador_objetos+=1
                                    print(contador_objetos, objetos[contador_objetos-1])
                                contador_objetos=0

                                opcion_usar=input("       --> ").lower()

                                if opcion_usar=="pollo con veneno" and pollo_envenenado==False and (". Veneno") in objetos:
                                   print("Enhorabuena, has mezclado el pollo con el veneno y has conseguido un pollo envenenado")

                                   objetos.remove(". Pollo")
                                   objetos.remove(". Veneno")
                                   objetos.append(". Pollo envenenado")
                                   pollo_envenenado=True

                                   input("Pulsa Enter para continuar")

                                if opcion_usar=="mapa":
                                   vuelta1=False
                                   break
                                   

                                else:
                                  print("Esos objetos no se pueden usar")
                                  input("Pulsa Enter para continuar")


                            case "3":
                                os.system("cls")
                                print(playa)
                                print(dar_intf)

                                for i in list(objetos):
                                    contador_objetos+=1
                                    print(contador_objetos, objetos[contador_objetos-1])
                                contador_objetos=0

                                opcion_dar=input("       --> ").lower()
                                print("No puedes dar este objeto")
                                input("Pulsa Enter para continuar")


                            case "4":
                                os.system("cls")
                                print(playa)
                                print(inventario_intf)

                                for i in list(objetos):
                                    contador_objetos+=1
                                    print(contador_objetos, objetos[contador_objetos-1])
                                contador_objetos=0

                                input("\nPulsa Enter para continuar")

                            case _:
                              print("Lo siento, está opción no está contemplada") 
              
                    pygame.mixer.music.stop()


input()




