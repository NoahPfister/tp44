# ici j'importe
import arcade

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# ici je met les couleurs
COLORS = [arcade.color.BLUE, arcade.color.FANDANGO_PINK,
        arcade.color.FRENCH_ROSE, arcade.color.GOLDEN_POPPY]


# je cree le cercle
class Cercle():
  def __init__(self, r, x, y, c, VarX, VarY):
      self.rayon = r
      self.centre_x = x
      self.centre_y = y
      self.color = c
      self.change_x = VarX
      self.change_y = VarY

  # je decine le cercle
  def draw(self):
      # arcade.draw_circle_filled(center_x, center_y, rayon, color)
      arcade.draw_circle_filled(self.centre_x, self.centre_y, self.rayon, self.color)
  #ceci fait bougeer le cercle
  def update(self):

     self.centre_x += self.change_x
     self.centre_y += self.change_y

     if self.centre_x < self.rayon:
         self.change_x *= -1
     if self.centre_x > SCREEN_WIDTH - self.rayon:
         self.change_x *= -1
     if self.centre_y < self.rayon:
         self.change_y *= -1
     if self.centre_y > SCREEN_HEIGHT - self.rayon:
         self.change_y *= -1

#je cree le rectangle
class Rectangle():
   def __init__(self, la, lo , x, y, c, VarX, VarY):
       self.largeur = la
       self.longueur = lo
       self.centre_x = x
       self.centre_y = y
       self.color = c
       self.change_x = VarX
       self.change_y = VarY

       # je decine le rectangle

   def draw(self):
       # arcade.draw_circle_filled(center_x, center_y, rayon, color)
       arcade.draw_rectangle_filled(self.centre_x, self.centre_y, self.largeur, self. longueur, self.color)
#ceci fait bouger le rectangle
   def update(self):

       self.centre_x += self.change_x
       self.centre_y += self.change_y

       if self.centre_x < self.largeur:
           self.change_x *= -1
       if self.centre_x > SCREEN_WIDTH - self.largeur:
           self.change_x *= -1
       if self.centre_y < self.longueur:
           self.change_y *= -1
       if self.centre_y > SCREEN_HEIGHT - self.longueur:
           self.change_y *= -1
# affichez le jeux
class MyGame(arcade.Window):
  def __init__(self):
      super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, "Exercice #1")
      self.liste_cercles = []
      self.liste_rectangle = []



  # definir cercle et rectangle
  def setup(self):
      # remplir la liste avec 20 objets de type Cercle
      for _ in range(20):
          rayon = random.randint(10, 50)
          center_x = random.randint(0 + rayon, SCREEN_WIDTH - rayon)
          center_y = random.randint(0 + rayon, SCREEN_HEIGHT - rayon)
          color = random.choice(COLORS)
          cercle = Cercle(rayon, center_x, center_y, color, 5,5)
          self.liste_cercles.append(cercle)
    #remplir liste avec 20 rectangle
      for _ in range(20):
           longeur = random.randint(10,50)
           largeur = random.randint(10,50)
           center_x = random.randint(0+largeur, SCREEN_WIDTH - largeur)
           center_y = random.randint(0+longeur, SCREEN_HEIGHT - longeur)
           color = random.choice(COLORS)
           rectangle = Rectangle(largeur,longeur, center_x, center_y, color, 5, 5)
           self.liste_rectangle.append(rectangle)

#commenceer le render


  def on_draw(self):
      arcade.start_render()

      for cercle in self.liste_cercles:
          cercle.draw()
          cercle.update()

      for rectangle in self.liste_rectangle:
          rectangle.draw()
          rectangle.update()

#faire en sorte de effacer lescercle


  def on_mouse_press(self, x: int, y: int, button: int, modifiers: int):
      if button == 1:
          for i in self.liste_cercles:
              maxpositionX = i.centre_x + i.rayon
              maxpositiponY = i.centre_y + i.rayon
              minpositionX = i.centre_x - i.rayon
              minpositionY = i.centre_y - i.rayon

              if maxpositionX > x > minpositionX and maxpositiponY > y > minpositionY:
                  self.liste_cercles.remove(i)

  # randomiser les couleurs
      elif button == 4:
          for i in self.liste_cercles:
              maxpositionX = i.centre_x + i.rayon
              maxpositiponY = i.centre_y + i.rayon
              minpositionX = i.centre_x - i.rayon
              minpositionY = i.centre_y - i.rayon

              if maxpositionX > x > minpositionX and maxpositiponY > y > minpositionY:
                  i.color = random.choice(COLORS)

#ceci est le jeux
def main():
  my_game = MyGame()
  my_game.setup()

  arcade.run()


main()

