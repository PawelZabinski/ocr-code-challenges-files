<script>
	import { onMount } from 'svelte';
  import { v4 as uuid } from 'uuid';
  import Header from './lib/Header.svelte';
  import DiaryEntryInput from './lib/DiaryEntryInput.svelte';
  import DiaryEntry from './lib/DiaryEntry.svelte';
	import NameField from './lib/NameField.svelte';
	
	let name = '';
  let search = '';
  let diaryEntries = [];

  $: diaryEntries = [...diaryEntries].sort((a, b) => {
      return a.timestamp < b.timestamp;
  })

  $: shownDiaryEntries = diaryEntries.filter(i => i.content.includes(search) || !search.length);

  // Used for margins
  let headerHeight;

  function handleLogOut() {
    name = '';
    search = '';
  }

  function publishDiaryEntry(e) {
    const diary = { content: e.detail.content, author: name, timestamp: new Date(), id: uuid() };
    diaryEntries = [...diaryEntries, diary];
  }
</script>

<Header bind:height={headerHeight} bind:search logOut={handleLogOut} />

<main style='--height: {headerHeight}px'>
	{#if name}
    <!-- Show input field for new diary entry -->
    <DiaryEntryInput on:publish={publishDiaryEntry} />

		<!-- Show all diary entries -->
    {#each shownDiaryEntries as diary (diary.id)}
      <DiaryEntry {diary}/>
    {:else}
      <p>Emptiness</p>
    {/each}
	{:else}
		<NameField bind:name />
	{/if}
</main>

<style>
  :global(body) {
    padding: 0;
    margin: 0;
    box-sizing: border-box;

    overflow-y: scroll;

    font-family: Arial;

    --primary: #232323;
    --accent: #4580cc;
		--background: #F9F9F9; 

    --width: min(90vw, 500px);
  }

	main {
		background-color: var(--background);
		min-height: 100vh;
		
		display: flex;
		flex-direction: column;

    justify-content: center;
    align-items: center;

    margin-top: var(--height);

    text-align: center;
	}

  main > * {
    width: var(--width);
  }

  p {
    color: #777;
  }
</style>