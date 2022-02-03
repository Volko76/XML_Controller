# XML_Controller

This controller allow to contruct a XML file ("merged.xml") from different XML sources (both online(url) and offline(file))

It ADD the XML sources to the main merged XML file

# Example:
We select a stylo.xml which look like this :
  <menu>
    <item>
      <id>1</id>
      <name>Fabercastel</name>
      <cost>10</cost>
      <description>1 mm pen</description>
    </item>
  </menu>
and a online url xml file like this https://api.androidhive.info/pizza/?format=xml

It will create a merged.xml file like this :
  <menu>
    <item>
      <id>1</id>
      <name>Fabercastel</name>
      <cost>10</cost>
      <description>1 mm pen</description>
    </item>
  </menu>
  <menu>
    <item>
      <id>1</id>
      <name>Margherita</name>
      <cost>155</cost>
      <description>Single cheese topping</description>
    </item>
    <item>
      <id>2</id>
      <name>Double Cheese Margherita</name>
      <cost>225</cost>
      <description>Loaded with Extra Cheese</description>
    </item>
  ... etc ...
    <item>
      <id>10</id>
      <name>Chicken Golden Delight</name>
      <cost>490</cost>
      <description>Golden corn, Double Barbeque and Cheese</description>
    </item>
  </menu>
  
And if we relaunch the program an other time with for example tennis.xml which look like this :
  <graphics card>
    <name>RTX 3090</name>
  </graphics card>    
  
We will get a merged.xml file like this :
<menu>
    <item>
      <id>1</id>
      <name>Fabercastel</name>
      <cost>10</cost>
      <description>1 mm pen</description>
    </item>
  </menu>
  <menu>
    <item>
      <id>1</id>
      <name>Margherita</name>
      <cost>155</cost>
      <description>Single cheese topping</description>
    </item>
    <item>
      <id>2</id>
      <name>Double Cheese Margherita</name>
      <cost>225</cost>
      <description>Loaded with Extra Cheese</description>
    </item>
  ... etc ...
    <item>
      <id>10</id>
      <name>Chicken Golden Delight</name>
      <cost>490</cost>
      <description>Golden corn, Double Barbeque and Cheese</description>
    </item>
  </menu>
  <graphics card>
    <name>RTX 3090</name>
  </graphics card>
