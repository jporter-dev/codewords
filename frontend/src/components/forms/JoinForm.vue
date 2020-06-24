<template>
  <v-fade-transition appear>
    <v-form
      ref="form"
      v-model="validForm"
      @submit.prevent="joinGame"
    >
      <v-card>
        <v-card-text>
          <v-row dense>
            <v-col md="4">
              <v-text-field
                :label="$t('room id')"
                :placeholder="$t('enter room id')"
                v-model="room_id"
                :rules="[rules.required, rules.id_length]"
                outlined
              ></v-text-field>
            </v-col>
            <v-col>
              <v-text-field
                :label="$t('secret agent name')"
                :placeholder="$t('enter name')"
                v-model="username"
                :rules="[rules.required, rules.name_length]"
                counter="20"
                outlined
              ></v-text-field>
            </v-col>
          </v-row>
          <v-btn
            block
            color="primary"
            large
            type="submit"
            @click.stop="joinGame"
          >{{ $t('join') }}</v-btn>
        </v-card-text>
      </v-card>
    </v-form>
  </v-fade-transition>
</template>

<script>
import { mapState, mapMutations } from "vuex";

export default {
  name: "create-form",
  data() {
    return {
      validForm: false,
      room_num: ""
    };
  },
  computed: {
    ...mapState(["rules"]),
    username: {
      get() {
        return this.$store.state.username;
      },
      set(v) {
        return this.$store.commit("set_username", v);
      }
    },
    room_id: {
      get() {
        return this.room_num.toUpperCase();
      },
      set(v) {
        this.room_num = v;
      }
    }
  },
  methods: {
    ...mapMutations(["set_username", "set_room"]),
    joinGame() {
      this.$refs.form.validate();
      if (this.validForm) {
        this.set_room(this.room_id);
        this.$router.push({ name: "Player", params: { room: this.room_id } });
      }
    }
  }
};
</script>
