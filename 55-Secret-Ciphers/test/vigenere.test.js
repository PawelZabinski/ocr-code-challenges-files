function vigenere(text, key, isEncoding) {
  const alphabet = 'abcdefghijklmnopqrstuvwxyz'.split('');
  
  let i = 0;

  const chars = text
    .split('')
    .map(char => {
      const indexOfChar = alphabet.indexOf(char.toLowerCase());

      // If character is not in the alphabet, return it
      if (indexOfChar === -1)
        return char;
      
      const indexOfKeyChar = alphabet.indexOf(key[i++ % key.length]);

      const newCharIndex = isEncoding ? indexOfChar + indexOfKeyChar : indexOfChar - indexOfKeyChar;
      const newChar = alphabet[(newCharIndex + alphabet.length) % alphabet.length];

      return char.toLowerCase() == char ? newChar : newChar.toUpperCase();
    });
  
  return chars.join('');
}

describe('Vigenere Cipher', () => {

  it('can encode a word', () => {
    const encrypted = vigenere('arise', 'key', true);

    expect(encrypted).toBe('kvgci');
  });

  it('can encode upper case', () => {
    const encrypted = vigenere('Computer science is the best', 'school', true);

    expect(encrypted).toBe('Uqtdiewt zqwpfel wg ezg isge');
  });

  it('can encode sentence', () => {
    const encrypted = vigenere('computer science is the best', 'school', true);

    expect(encrypted).toBe('uqtdiewt zqwpfel wg ezg isge');
  });

  it('can decode a word', () => {
    const decrypted = vigenere('rmwlqb', 'code', false);

    expect(decrypted).toBe('python');
  });

  it('can decode a sentence', () => {
    const decrypted = vigenere('A ap wxswrlwnfanj lhh hhhfopwnrf oi vesjevkirf', 'sad', false);
    
    expect(decrypted).toBe('I am experiencing the phenomenon of depression');
  });

});