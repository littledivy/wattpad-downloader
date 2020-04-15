<template>
    <b-navbar>
        <template slot="brand">
            <b-navbar-item>
            <b-icon
                pack="fas"
                icon="user"
                size="is-small">
            </b-icon>
            <b><img src="logo.png" /></b>
            </b-navbar-item>
        </template>
        <template slot="end">
            <b-navbar-item tag="div">
                <div class="buttons">
                    <a class="button is-primary">
                        <strong>Github</strong>
                    </a>
                </div>
            </b-navbar-item>
        </template>
    </b-navbar>
</template>
