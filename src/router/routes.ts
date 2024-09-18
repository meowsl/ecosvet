import { RouteRecordRaw } from 'vue-router';

const routes: RouteRecordRaw[] = [
    {
        path: '/',
        component: () => import('layouts/MainLayout.vue'),
        children: [{ path: '', name: 'IndexPage', component: () => import('pages/index/IndexPage.vue') }],
    },
    {
        path: '/about',
        component: () => import('layouts/MainLayout.vue'),
        children: [{ path: '', name: 'AboutPage', component: () => import('pages/about-us/AboutPage.vue') }],
    },
    {
        path: '/blog',
        component: () => import('layouts/MainLayout.vue'),
        children: [{ path: '', name: 'BlogPage', component: () => import('pages/blog/BlogPage.vue') }],
    },
    {
        path: '/news',
        component: () => import('layouts/MainLayout.vue'),
        children: [{ path: '', name: 'NewsPage', component: () => import('pages/news/NewsPage.vue') }],
    },
    {
        path: '/profile',
        component: () => import('layouts/MainLayout.vue'),
        children: [{ path: '', name: 'ProfilePage', component: () => import('pages/profile/ProfilePage.vue') }],
    },

    // Always leave this as last one,
    // but you can also remove it
    {
        path: '/:catchAll(.*)*',
        component: () => import('pages/ErrorNotFound.vue'),
    },
];

export default routes;
