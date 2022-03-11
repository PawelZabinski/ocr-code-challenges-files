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

describe('Vernan Cipher', () => {

  it('can encode a word', () => {
    expect(vernan('hello', 'pluto')).toBe('8)98 ')
    expect(vernan('programming', '#2dk4dfhsdf')).toBe("s`+,f%+%:*!")
  })

  it('can handle upper case', () => {
    expect(vernan('Donkey', 'ocr-code')).toBe('-,<f&6')
  })

  it('can encode a sentence', () => {
    expect(vernan('i can read', 'oheivds32n')).toBe('&h&(8d!vs*')
  })

  it('can decode a word', () => {
    expect(vernan('8)98 ', 'pluto')).toBe('hello')
    expect(vernan("s`+,f%+%:*!", '#2dk4dfhsdf')).toBe("programming")
  })

  it('can decode a sentence', () => {
    expect(vernan('&h&(8d!vs*', 'oheivds32n')).toBe('i can read')
  })
});