Bezpečnostní kamera řízená pomocí Raspberry Pi Zero. Schopná detekovat pohyb a následně nahrát.

server.py - hlavní program, který běží na frameworku Flask - hostuje webovou aplikaci, posílá requesty na webovou stránku a zpět získává data, které používá na změnu polohy serv, co uživatel napsal a chtěl, aby bylo přehráno

.idea - složka, která neobsahuje nic podstatného, co by bylo spojeno s hlavním programem, je to nastavení virtuálního prostředí

static - obsahuje podsložku css, která obsahuje stylování webové stránky
       - obsahuje podsložku image, která obsahuje všechny obrázky, které jsou používány na webové stránce
       - obsahuje podsložku js, která obsahuje javascripty, které slouží k interakci se stránkou a kamerou 

templates:
       - obsahuje soubor base.html, který je šablona pro následující soubory:
       - camera.html - karta, která slouží k pohybu se servy a streamování obrazu z kamery, v budoucnu bude také možné zaznamenávat video a dělat fotky pomocí tlačítek 
       - index.html - úvodní karta, která se zobrazí po zadání IP adresy do prohlížeče
       - text_to_speech.html - karta, která pomocí textu na mluvení dokáže komunikovat s návštěvníkem kamery, v budoucnu bych chtěl tuto kartu sloučit s kartou camera.html
          
camera.py - soubor se třídou (class) na ovládní a nastavení kamery          
          
data.txt - soubor, do kterého se ukládají hodnoty pozic obou servo motorů a krok, o který se budou hodnoty zvyšovat

functions.py - balíček všech funkcí (čtení a psaní do textových dokumentů, generování kamerového signálu, pohyb serv), použitých v hlavním programu

servo.py - testovací funkce na pohyb serv

test.py - testovací soubor na pohyb serv
