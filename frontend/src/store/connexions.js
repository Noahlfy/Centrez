import reactive from 'vue';
import {api} from '@/services/api.js';


export const user_connexions = reactive({
    user_id: null,
    user_username: null,
    user_email: null,
    user_first_name: null,
    user_last_name: null,
});

export const asso_connexions = reactive({
    asso_id: null,
    asso_name: null,
});