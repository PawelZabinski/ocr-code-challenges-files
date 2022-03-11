<script>
  // Regex Query Tool
  
  // This is a tool that allows the user to enter a text string and then in a separate text box enter a regex pattern. It will run the regular expression against the string and return any
  // matches or flag errors in the regular expression.

  let text = ''
  let regex = ''
	
	let allMatches = []
	
	let isValidRegex = false
	
	$: {
		try {
			const pattern = new RegExp(regex, 'g')
			allMatches = [...text.matchAll(pattern)].filter(i => i != "");
			isValidRegex = true
		} catch {
			isValidRegex = false
			allMatches = []
		}
	}
</script>

<main>
  <section>
    <p class='label'>Text</p>
    <textarea bind:value={text} />

    <p class='label'>Regex Pattern</p>
    <input class={isValidRegex ? '' : 'error'} type=text bind:value={regex} />
  </section>

  {#each allMatches as match}
		<li>{match}</li>
	{/each}
</main>

<style>
  main {
    font-family: Arial;
      
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;

    min-width: 100vw;
    min-height: 100vh;
  }

  section {
    display: flex;
    flex-direction: column;
    align-items: center;

    margin-bottom: 3rem;
  }

  input, textarea {
    resize: none;
    width: 80vw;

    padding: 1rem;

    border: solid #eee 2px;
    border-radius: 10px;

    background-color: white;
  }

  .error {
    background-color: #FF6666;
    border-color: #F73737;
    color: white;
  }

  .label {
    margin: .2rem;
    margin-right: auto;
    margin-left: .25rem;
  }

  textarea {
    height: 15vh;
    margin-bottom: .5rem;
  }
</style>