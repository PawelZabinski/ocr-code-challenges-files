<script>
	export let name;
	
	let value
	
	function handleSubmit() {
		name = value
	}
</script>

<form on:submit|preventDefault={handleSubmit}>
	<input id='nameField' type=text bind:value placeholder='Enter your name'/>
	<input id='submit' type=submit/>
</form>

<style>
	form {
		display: flex;
		flex-direction: column;
		
		justify-content: space-between;
		align-items: center;
		
		width: min(80%, 400px);
		height: 100%;
	}

  #nameField {
    text-align: center;

		background-color: white;

    border: none;
    border-radius: 8px;

    box-shadow: 0 5px 10px rgba(0, 0, 0, 0.12);
			
		width: 100%;
    height: 3.5em;

    margin-bottom: 1.5em;

    font-size: .8rem;
  }
	
	#submit {
		color: white;
		background-color: var(--accent);

    border: none;
    border-radius: 8px;
			
		width: 100%;
    height: 3.5em;

    font-size: .8rem;

    cursor: pointer;
	}
</style>