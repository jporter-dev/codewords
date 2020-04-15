<template>
  <v-layout align-start justify-center row fill-height>
    <v-flex md6>
      <v-card tile flat>
        <v-card-text px-0 class='text-xs-left'>
          <h4>{{$t('getting started')}}</h4>
          <p>
            {{ $t('getting started directions')}}
          </p>
          <h4 class="header">{{ $t('how to play') }}</h4>
          <p>{{ $t('how to play instructions') }}</p>
          <p>
            <a href="https://www.youtube.com/watch?v=zQVHkl8oQEU">{{ $t('watch instructions') }}</a>
          </p>
        </v-card-text>
      </v-card>
    </v-flex>
  </v-layout>
</template>

<script>
export default {
  name: 'help',
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
</style>
