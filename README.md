<h1> Bezpečnostní kamera </h1> 

Bezpečnostní kamera řízená pomocí Raspberry Pi Zero. Schopná detekovat pohyb a následně nahrát

<h3>server.py</h2> 
<blockquote>- hlavní program, který běží na frameworku Flask - hostuje webovou aplikaci, posílá requesty na webovou stránku a zpět získává data, které používá na změnu polohy serv, co uživatel napsal a chtěl, aby bylo přehráno</blockquote>

<h3>.idea</h3>
<blockquote>- složka, která neobsahuje nic podstatného, co by bylo spojeno s hlavním programem, je to nastavení virtuálního prostředí</blockquote>

<h3>static</h3>
<ul> 
       <blockquote><li>obsahuje podsložku css, která obsahuje stylování webové stránky</li><br>
       <li>obsahuje podsložku image, která obsahuje všechny obrázky, které jsou používány na webové stránce</li><br>
       <li>obsahuje podsložku js, která obsahuje javascripty, které slouží k interakci se stránkou a kamerou</li><br></blockquote> 
</ul>

<h3>templates</h3>
<ul>
<blockquote><li>obsahuje soubor base.html, který je šablona pro následující soubory:</li><br>
<li>camera.html - karta, která slouží k pohybu se servy a streamování obrazu z kamery, v budoucnu bude také možné zaznamenávat video a dělat fotky pomocí tlačítek</li><br>
<li>index.html - úvodní karta, která se zobrazí po zadání IP adresy do prohlížeče</li><br>
<li>text_to_speech.html - karta, která pomocí textu na mluvení dokáže komunikovat s návštěvníkem kamery, v budoucnu bych chtěl tuto kartu sloučit s kartou camera.html</li><br></blockquote>
</ul> 

<h3>camera.py</h3>
<blockquote>- soubor se třídou (class) na ovládní a nastavení kamery</blockquote>          
          
<h3>data.txt</h3> 
<blockquote>- soubor, do kterého se ukládají hodnoty pozic obou servo motorů a krok, o který se budou hodnoty zvyšovat</blockquote>

<h3>functions.py</h3> 
<blockquote>- balíček všech funkcí (čtení a psaní do textových dokumentů, generování kamerového signálu, pohyb serv), použitých v hlavním programu</blockquote>

<h3>servo.py</h3>
<blockquote>- testovací funkce na pohyb serv</blockquote>

<h3>test.py</h3> 
<blockquote>- testovací soubor na pohyb serv</blockquote>
