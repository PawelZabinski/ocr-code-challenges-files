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

describe('Ceasar Cipher', () => {

  it('can encode a word', () => {
    expect(ceasar('hello', 7, true)).toBe('olssv')
  });

  it('can encode an upper case', () => {
    expect(ceasar('JavaScript', 3, true)).toBe('MdydVfulsw')
  });

  it('can encode a sentence', () => {
    expect(ceasar('my friend is very lonely', 13, true)).toBe('zl sevraq vf irel ybaryl')
  })

  it('can decode a word', () => {
    expect(ceasar('olssv', 7, false)).toBe('hello')
  });

  it('can decode an upper case', () => {
    expect(ceasar('MdydVfulsw', 3, false)).toBe('JavaScript')
  });

  it('can decode a sentence', () => {
    expect(ceasar('zl sevraq vf irel ybaryl', 13, false)).toBe('my friend is very lonely')
  })

});