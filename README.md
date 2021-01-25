<h1> Bezpečnostní kamera </h1> 

Bezpečnostní kamera řízená pomocí Raspberry Pi. Schopná detekovat pohyb a následně nahrát

<a href="server.py"><h3>server.py</h2></a>
 <ol>- hlavní program, který běží na frameworku Flask - hostuje webovou aplikaci, posílá requesty na webovou stránku a zpět získává data, které používá na změnu polohy serv; co uživatel napsal a chtěl, aby bylo přehráno</ol>

<a href=".idea"><h3>.idea</h3></a>
<ol>- složka, která neobsahuje nic podstatného, co by bylo spojeno s hlavním programem, je to nastavení virtuálního prostředí</ol>

<a href="static"><h3>static</h3></a>

<ol>
- obsahuje podsložku <a href="static/css/style.css">css</a>, která obsahuje stylování webové stránky<br>
- obsahuje podsložku <a href="static/image">image</a>, která obsahuje všechny obrázky, které jsou používány na webové stránce<br>
- obsahuje podsložku <a href="static/js/functions.js">js</a>, která obsahuje javascripty, které slouží k interakci se stránkou a kamerou
</ol>


<a href="templates"><h3>templates</h3></a>

<ol>
 &#x25FC; </div>obsahuje soubor <a href="templates/base.html">base.html</a>, který je šablona pro následující soubory:<br><br>
 <ol><ol>
 <a href="templates/camera.html">&#x25BC; camera.html</a> - soubor, který slouží k pohybu se servy a streamování obrazu z kamery, v budoucnu bude také možné zaznamenávat video a dělat fotky pomocí tlačítek<br><br>
  
 <a href="templates/index.html">&#x25BC; index.html</a> - úvodní soubor, který se zobrazí po zadání IP adresy do prohlížeče<br><br>
 
 <a href="templates/text_to_speech">&#x25BC; text_to_speech.html</a> - soubor, který pomocí textu na mluvení dokáže komunikovat s návštěvníkem kamery, v budoucnu bych chtěl tuto kartu sloučit s kartou camera.html
 </ol></ol>
</ol>


<a href="camera.py"><h3>camera.py</h3></a>
<ol>- soubor se třídou (class) na ovládní a nastavení kamery</ol>          
          
<a href="data.txt"><h3>data.txt</h3></a> 
<ol>
- soubor, do kterého se ukládají hodnoty pozic obou servo motorů a krok, o který se budou hodnoty zvyšovat
</ol>

<a href="functions.py"><h3>functions.py</h3></a>
<ol>
- balíček všech funkcí (čtení a psaní do textových dokumentů, generování kamerového signálu, pohyb serv), použitých v hlavním programu
</ol>

<a href="servo.py"><h3>servo.py</h3></a>
<ol>
- testovací funkce na pohyb serv
</ol>

<a href="test.py"><h3>test.py</h3></a>
<ol>
- testovací soubor na pohyb serv
</ol>
