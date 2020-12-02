<h1> Bezpečnostní kamera </h1> 

Bezpečnostní kamera řízená pomocí Raspberry Pi Zero. Schopná detekovat pohyb a následně nahrát

<h3>server.py</h2> 
 <ol>- hlavní program, který běží na frameworku Flask - hostuje webovou aplikaci, posílá requesty na webovou stránku a zpět získává data, které používá na změnu polohy serv, co uživatel napsal a chtěl, aby bylo přehráno</ol>

<h3>.idea</h3>
<ol>- složka, která neobsahuje nic podstatného, co by bylo spojeno s hlavním programem, je to nastavení virtuálního prostředí</ol>

<h3>static</h3>

<ol>
- obsahuje podsložku css, která obsahuje stylování webové stránky<br>
- obsahuje podsložku image, která obsahuje všechny obrázky, které jsou používány na webové stránce<br>
- obsahuje podsložku js, která obsahuje javascripty, které slouží k interakci se stránkou a kamerou
</ol>


<h3>templates</h3>

<ol>
- obsahuje soubor base.html, který je šablona pro následující soubory:
 <ol>
- camera.html - karta, která slouží k pohybu se servy a streamování obrazu z kamery, v budoucnu bude také možné zaznamenávat video a dělat fotky pomocí tlačítek<br><br>
- index.html - úvodní karta, která se zobrazí po zadání IP adresy do prohlížeče<br>
- text_to_speech.html - karta, která pomocí textu na mluvení dokáže komunikovat s návštěvníkem kamery, v budoucnu bych chtěl tuto kartu sloučit s kartou camera.html
 </ol>
</ol>


<h3>camera.py</h3>
<ol>- soubor se třídou (class) na ovládní a nastavení kamery</ol>          
          
<h3>data.txt</h3> 
<ol>
- soubor, do kterého se ukládají hodnoty pozic obou servo motorů a krok, o který se budou hodnoty zvyšovat
</ol>

<h3>functions.py</h3> 
<ol>
- balíček všech funkcí (čtení a psaní do textových dokumentů, generování kamerového signálu, pohyb serv), použitých v hlavním programu
</ol>

<h3>servo.py</h3>
<ol>
- testovací funkce na pohyb serv
</ol>

<h3>test.py</h3> 
<ol>
- testovací soubor na pohyb serv
</ol>
