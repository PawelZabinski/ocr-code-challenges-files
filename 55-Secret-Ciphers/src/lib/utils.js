const alphabet = 'abcdefghijklmnopqrstuvwxyz'.split('');

function vigenere(text, key, isEncoding) {
  let i = 0;

  const chars = text
    .split('')
    .map(char => {
      const indexOfChar = alphabet.indexOf(char.toLowerCase());

      if (indexOfChar === -1)
        return char;
      
      const indexOfKeyChar = alphabet.indexOf(key[i++ % key.length]);

      const newCharIndex = isEncoding ? indexOfChar + indexOfKeyChar : indexOfChar - indexOfKeyChar;
      const newChar = alphabet[(newCharIndex + alphabet.length) % alphabet.length];

      return char.toLowerCase() == char ? newChar : newChar.toUpperCase();
    });
  
  return chars.join('');
}

function vernan(text, key) {
  const ascii = Array
    .from(Array(126 - 32).keys())
    .map(i => i + 32)
    .map(i => String.fromCharCode(i));

  return text
    .split('')
    .map((char, i) => {
      const charCode = ascii.indexOf(char);
      const keyCode = ascii.indexOf(key[i % key.length]);

      return ascii[(charCode ^ keyCode) % ascii.length];
    })
    .join('')
}

function ceasar(text, key, isEncoding) {
  const alphabet = 'abcdefghijklmnopqrstuvwxyz'.split('');

  return text
    .split('')
    .map(char => {
      const charIndex = alphabet.indexOf(char.toLowerCase());

      if (charIndex === -1)
        return char

      const newCharCode = isEncoding ? charIndex + key : charIndex - key;
      const newChar = alphabet[(newCharCode + 26) % alphabet.length];

      return char == char.toLowerCase() ? newChar : newChar.toUpperCase();
    })
    .join('')
}


export { vigenere, vernan, ceasar };