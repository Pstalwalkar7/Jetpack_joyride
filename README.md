Coded by: PUSHKAR TALWALKAR
Roll No : 2018101010


Contents:

1. Rules of the game
2. Description of classes created
3. Requirements
4. Special Features


Rules of the Game:

0. USE small case only(disable caps lock) to control your character: 
   a : move left
   d : move right
   w : move up (jetpack)
   q : quit the game
   Spacebar : Activate shield for 10 seconds. It takes 60 seconds to recharge the shield

1. You have 3 lives. Reach to the end of the game, beat the boss enemy, and win the game.
2. You have to finish the game in 100 seconds, else you lose.
3. Collect coins to get more points.
4. The Magnet (M) attracts  the player towards it when in it's range.
5. The SpeedUp (P) speeds up the game and the character motions
6. The zappers (in *) take your lives. 
7. The boss enemy is tricky; he follows your motion and shoots snowballs at you.
8. The boss enemy cannot be touched without losing a life.
9. The boss can be shot by your bullets.


Description of the Classes created:

The game is structured as follows:
   1. Person : Any movable object
   2. Bullet(Person) : The bullet of the hero, Mandalorian
   3. Snowball(Person) : The snowball thrown by the boss
   4. Mandalorian(Person) : The hero
   5. Enemy(Person) : The boss enemy
   6. Coins : Coins in the grid
   7. Board : The Board as a whole. 
   8. Magnet(Coins) : The magnet which attracts the player.
   9. Powerup(Magnet) : The speed up powerup 
   10. Alarmhandler : Handles errors in input
   11. _getChUnix : Takes asynchronous input 
   12. Ground : Creates the ground in the board of the game
   13. Zapper : Creates the zappers/laser beams in the game. This is the most common obstacle. 
   14. Engine(Board,Mandalorian,Enemy,Bullet,Magnet,Coins,Ground,Zapper,Snowball) : The game in its entirety.


Instructions to run game:

1. Download the repository.
2. In the folder, run the command in terminal :
   python3 Game.py


Requirements:

1. Python3
2. Colorama library (install by:"pip3 install colorama")

Special Features:

1. Colors are used.
2. Zapper of one more type : 135 degrees with the ground are created.
3. Well structured boss.
4. There is a secret hack to reach the boss directly, avoiding all the obstacles. (Hint: Try the numbers on the keyboard)
