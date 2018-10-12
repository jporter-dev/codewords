import { shallowMount, createLocalVue } from '@vue/test-utils'
import Vuetify from 'vuetify'
import CreateForm from '@/components/CreateForm.vue'

const localVue = createLocalVue()
localVue.use(Vuetify)

describe('CreateForm.vue', () => {
  it('renders some content', () => {
    // const wrapper = shallowMount(CreateForm, {localVue})
    // expect(wrapper.text().length).toBeTruthy()
  })
})
