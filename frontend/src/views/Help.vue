<template>
  <v-container>
    <v-row>
      <v-card tile>
        <v-card-title>How to Play</v-card-title>
        <v-card-text>
          <h4>Getting Started</h4>
          <p>
            This application is designed to be played on multiple devices. The "agent"
            view can be loaded on a TV or mobile devies, and the "spymaster" view
            should be activated on the phones of the spymasters.
          </p>
          <ol>
            <li>Create a game by pressing the "Create Game" button</li>
            <li>Optionally, select an alternative dictionary to play with. (Default: English)</li>
            <li>Other players can now join using the room code in the top left.</li>
            <li>Divide players into two teams and select one spymaster per team.</li>
            <li>The two spymasters shall now click to the "spymaster" view to see the color-coded board.</li>
            <li>The team that starts is highlighted at the top.</li>
            <li>The first spymaster shall come up with a number and a single-word codeword to link together as many cards as possible.</li>
            <li>Spymasters can click the cards to flip them as the agents guess.</li>
            <li>An agent guessing the enemy team's card or a citizen card ends the turn. Assassin ends the game.</li>
            <li>Repeat steps 7-9 alternating teams.</li>
            <li>The first team to clear their cards wins.</li>
          </ol>
          <br>
          For more info, read the <a href="https://en.wikipedia.org/wiki/Codenames_(board_game)#Rules">Wikipedia rules page...</a>
        </v-card-text>
      </v-card>
    </v-row>
  </v-container>
</template>
