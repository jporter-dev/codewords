<template>
  <v-container>
    <v-row>
      <v-card tile>
        <v-card-title>{{ $t("how to play") }}</v-card-title>
        <v-card-text>
          <h4>{{ $t('getting started') }}</h4>
          <p>
            {{ $t('getting started directions') }}
          </p>
          <ol>
            <li>{{ $t('step 1') }}</li>
            <li>{{ $t('step 2') }}</li>
            <li>{{ $t('step 3') }}</li>
            <li>{{ $t('step 4') }}</li>
            <li>{{ $t('step 5') }}</li>
            <li>{{ $t('step 6') }}</li>
            <li>{{ $t('step 7') }}</li>
            <li>{{ $t('step 8') }}</li>
            <li>{{ $t('step 9') }}</li>
            <li>{{ $t('step 10') }}</li>
            <li>{{ $t('step 11') }}</li>
          </ol>
          <br>
          {{ $t('for more info read pt1') }}<a href="https://en.wikipedia.org/wiki/Codenames_(board_game)#Rules">{{ $t('for more info read pt2') }}</a>
        </v-card-text>
      </v-card>
    </v-row>
  </v-container>
</template>

<i18n src="@/plugins/translations/help.json"/>