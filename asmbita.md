# Assembly Basics ITA

The following is a document originally made to help some classmates of mine understand the assembly language a bit better (and it also serves the purpose of notes in my case); if you somehow stumble upon this, please leave this page and move on with your day.

Per il resto di voi coglioni:

--------------------------------------------------------------------------------

# Assembly

## Alcune info generali:

- questo linguaggio non è Case-Sentitive (ergo non presta attenzione a maiuscolo o minuscolo)
- si possono inserire tre tipi di numeri in assembly:
- - Decimali, immettendo semplicemente il valore oppure accompagnandolo con una `d`

- - - Esempio dichiarando una variabile: `var db 10d` oppure `var db 10`

- - Esadecimali, immettendo il valore accompagnato da una `h`:

- - - Esempio dichiarando una variabile: `var db 10h` (10h = 16)

## Dichiarazioni

- `< nome var > < tipo > < valore >`
- - ove < tipo > può essere:

- - - DB ;Declare Byte, la variabile occupa 8 bit.

- - - DW ;Declare Word, la variabile occupa 16 bit.

- - - DD ;Declare Double Word, la variabile occupa 32 bit.

- - ove < valore > può essere:

- - - `?` per indicare che questa variabile non ha un valore definito;

- - - `< numero >`

- `< nome etichetta >:` per dichiarare una sezione di codice a cui fare riferimento, solitamente da terminare con `end < nome etichetta >` oppure `loop < nome etichetta >`

## Vari Comandi

- INC < op > `;equiv. ad "i++" di C++, incrementa (di uno) < op >`
- DEC < op > `;equiv. ad "i--" di C++, decrementa (di uno) < op >`
- MUL < op > `;moltiplica AX per < op >` <!-- - IMUL < op > ;moltiplica AX per < op >, con segno -->
- DIV < op > `;divide AX per < op >`
- Resto in AH, Quoziente in AL <!-- - IDIV < op > ;divide AX per < op >, con segno --> 
- ADD < op1 >, < op2 > `;somma < op2 > a < op1 >`
- SUB < op1 >, < op2 > `;sottrae < op2 > a < op1 >`
- LEA < op1 >, < op2 > `;copia l'indirizzo di < op2 > in < op1 >`
- MOV < op1 >, < op2 > `;copia < op2 > in < op1 >`
- - Valori di AH fino ad ora usati (`mov ah, < uno di questi >`):

- - - `02h`: stampa un carattere contenuto in DL

- - - `01h`: acquisisce un singolo carattere, non è necessario premere invio.

- - - `09h`: stampa il contenuto di DX, solitamente una stringa che termina con `$`

- - - `4Ch`: termina il programma

- - `< op2 > da prefacciare con una chiocciola (@) quando si sposta DATA in AX`

- LOOP < nome etichetta > `;ripete il codice associato all'etichetta`

- END < nome etichetta > `;termina il codice associato all'etichetta`

- INT < op > `;fa una richiesta al S.O.` <!-- ADC -->

- - Valori di < op > fino ad ora a noi noti:

- - - `21h`: legge il contenuto di AH

- CMP < op1 >, < op2 > `;compara <op2> in funzione di <op2>, si usa per condizionali insieme alle istruzioni di salto`

## Istruzioni di salto

Nelle istruzioni seguenti:

- < op > è un etichetta
- le istruzioni sono composte da:
- - J, per Jump, Salta

- - A, per Above, Sopra `( PER NUMERI SENZA SEGNO )`

- - B, per Below, Sotto `( PER NUMERI SENZA SEGNO )`

- - C, per Carry, Riporto

- - N, per Not, Nega

- - G, per Greater, di più

- - L, per Less, di meno

- - E, per Equals, Equivalente

Le istruzioni:

### Base

- JA < op > `;Salta se, nel CMP, < op2 > è maggiore di < op1 >`
- JAE < op > `;Salta se, nel CMP, < op2 > è maggiore/uguale di < op1 >`
- JB < op > `;Salta se, nel CMP, < op2 > è minore di < op1 >`
- JBE < op > `;Salta se, nel CMP, < op2 > è minore/uguale di < op1 >`
- JC < op > `;Salta se, nel CMP, < op2 > è maggiore di < op1 >`
- JE < op > `;Salta se, nel CMP, < op2 > è uguale di < op1 >`
- JG < op > `;Salta se, nel CMP, < op2 > è maggiore di < op1 >` ( mantiene i segni )
- JGE < op > `;Salta se, nel CMP, < op2 > è maggiore/uguale di < op1 >` ( mantiene i segni )
- JL < op > `;Salta se, nel CMP, < op2 > è minore di < op1 >` ( mantiene i segni )
- JLE < op > `;Salta se, nel CMP, < op2 > è minore/uguale di < op1 >` ( mantiene i segni )

### Negate

- JNA < op >
- JNAE < op >
- JNB < op >
- JNBE < op >
- JNC < op >
- JNE < op >
- JNG < op >
- JNGE < op >
- JNL < op >
- JNLE < op >

## Pezzi di programma

# In conclusione

Ringraziarmi non farebbe male a nessuno.
