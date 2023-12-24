Pie projekta strādāja:<br>
Artjoms Fomins 231RDB152 9. grupa

## Problēmas apraksts:<br>
Es vadu google sheets finanšu pārskatu par visiem saviem izdevumiem. Katru mēnesi es saņemu algu par iepriekšējo mēnesi un man jāiet uz vietni visma.hop un ņemt no turienes savi dati. Tad es ieju uz google sheet un veidoju jaunu atskaiti par jauno mēnesi. Kopumā dažreiz tas aizņem daudz laika un tāpēc es nolēmu to automatizēt. Saņemšana savu pašreizējo algu un automātiski izveidojot jaunu pārskatu par jauno mēnesi

## Izmantotās bibliotēkas:<br>
- <code>selenium</code> - informācijas iegūšana par savu algu hop.visma<br>
- <code>time</code> - lieto kopā ar selenium. Izmanto, lai pauzētu starp vietnes loģiku
- <code>os</code> - jo projektā tiek izmantoti mani personas dati, piemēram, e-pasts, parole, ID google sheet dokuments, es to glabāju <code>.env</code> failā, kurš ir ignorēts ar <code>.gitgnore</code>. <code>os</code> tiek izmantots lai lasīt enviroment mainīgos no <code>.env</code> faila. Projektā ir piemērs <code>.env.sample</code>, ka tas izskatās.<br>
- <code>dotenv</code> - lejupielādēt enviroment mainīgos no <code>.env</code> faila
- <code>datetime</code> - lai noteikt, kāds ir tagad mēnesis un gads.
- <code>sys</code> - lai pabeigt faila izpildi, ja trūkst kaut kādi dati   
- google bibleotēkas
    - <code>google.oauth2.credentials</code> - ielādēt vai izveidot OAuth2 credentials datus, lai piekļūtu google sheets api
    - <code>google.auth.transport.requests</code> - bibliotēka ir atbildīga par HTTP pieprasījumu apstrādi google pakalpojumos 
    - <code>google_auth_oauthlib.flow</code> - bibliotēka, lai sāktu OAuth0 autorizācijas plūsmu instalētai lietojumprogrammai
    - <code>googleapiclient.discovery</code> - bibliotēka, lai izveidot objektu mijiedarbībai ar google sheet api

## Projeksta struktūra
<code>.env.sample</code> - faila piemērs, ka es glābāju parsonas datus.<br>
<code>salary.py</code> - tur ir visa loģika, kas saistīta ar algu informācijas iegūšanu. <br>
<code>months.py</code> - fails, kurā es izveidoju nosaukumu savam jaunajam pārskatam, pamatojoties uz pašreizējo mēnesi un gadu<br>
<code>main.py</code> - galvenais fails, kurā es piekļūstu savam google sheet dokumentam, izveidoju jaunu pārskatu un saglabāju datus