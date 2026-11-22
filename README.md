# Project 1 - Cryptography

Permutation cipher (encryption + decryption) written in Python, console version.

Student ID: 161462 -> 161462 mod 3 = 2 -> **permutation cipher**.

## How to run

Python 3 is needed, no extra libraries.

```
python szyfr.py
```

After start you see the menu:

```
1. Encrypt
2. Decrypt
3. Show permutation
0. Exit
Choose an option:
```

## How the cipher works

The permutation is hardcoded in the code:

```python
PERM = [2, 0, 4, 1, 5, 3]
```

Its length is 6, so the text is split into blocks of 6 letters.
In every block the letters change places. Position `i` in the ciphertext
gets the letter from position `PERM[i]` in the plaintext (positions are counted from 0).

### Example step by step - encryption of `HELLOWORLD`

1. Text has 10 letters, 10 is not a multiple of 6, so we add `X` at the end:
   `HELLOWORLDXX`
2. Split into blocks: `HELLOW` and `ORLDXX`
3. First block `HELLOW`:

| position in plaintext | 0 | 1 | 2 | 3 | 4 | 5 |
|---|---|---|---|---|---|---|
| letter | H | E | L | L | O | W |

| position in ciphertext (i) | 0 | 1 | 2 | 3 | 4 | 5 |
|---|---|---|---|---|---|---|
| PERM[i] | 2 | 0 | 4 | 1 | 5 | 3 |
| letter | L | H | O | E | W | L |

   So `HELLOW` -> `LHOEWL`
4. Second block `ORLDXX` -> `LOXRXD`
5. Result: `LHOEWLLOXRXD`

### Decryption

Decryption does the opposite: the letter from position `i` of the ciphertext
goes back to position `PERM[i]`. At the end the padding `X` letters are removed.

`LHOEWLLOXRXD` -> `HELLOWORLD`

## Examples

| Input | Plaintext after preparing | Ciphertext |
|---|---|---|
| `Ala ma kota` | `ALAMAKOTA` | `AAALKMAOXTXX` |
| `HELLOWORLD` | `HELLOWORLD` | `LHOEWLLOXRXD` |
| `CRYPTOGRAPHY` | `CRYPTOGRAPHY` | `YCTROPAGHRYP` |
| `Attack at dawn` | `ATTACKATDAWN` | `TACTKADAWTNA` |

Spaces are removed and small letters are changed to capital letters.

Example session:

```
Choose an option: 1
Enter plaintext: Attack at dawn
Ciphertext: TACTKADAWTNA

Choose an option: 2
Enter ciphertext: TACTKADAWTNA
Plaintext: ATTACKATDAWN
```

## Error handling

The program does not crash, it shows the error and goes back to the menu.

| What user does | Message |
|---|---|
| empty text | `Error: Text cannot be empty.` |
| Polish letters, digits, other signs (`zażółć`, `abc123`) | `Error: Invalid character: '1'. Only letters A-Z and spaces are allowed.` |
| ciphertext with wrong length (`ABC`) | `Error: Ciphertext length must be a multiple of 6 (it is 3).` |
| wrong menu option (`7`) | `There is no such option. Choose 0, 1, 2 or 3.` |
| Ctrl+C | program ends with `Goodbye.` |

At start the program also checks if the permutation itself is correct
(at least 6 elements, numbers 0..n-1 without repeats).

## Code structure

| Function | What it does |
|---|---|
| `check_permutation()` | checks if `PERM` is a valid permutation |
| `prepare_text()` | removes spaces, makes capital letters, checks if only A-Z |
| `encrypt()` | adds `X` padding and changes letters in every block |
| `decrypt()` | checks length, reverses the permutation, removes `X` padding |
| `menu()` | prints the menu and reads the option |
| `main()` | main loop, calls functions and catches errors |

## Limitation

If the plaintext ends with the letter `X`, after decryption this `X` is removed
together with the padding (for example `RELAX` -> `RELA`).
