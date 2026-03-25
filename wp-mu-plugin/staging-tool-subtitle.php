<?php
/**
 * Custom REST endpoint for the staging tool to set the ACF sub_title field.
 *
 * Install: copy this file to wp-content/mu-plugins/staging-tool-subtitle.php
 * on the WordPress server. The mu-plugins folder auto-loads — no activation needed.
 */
add_action('rest_api_init', function () {
    register_rest_route('parentdata/v1', '/set-subtitle', [
        'methods'  => 'POST',
        'callback' => function ($request) {
            $post_id  = intval($request->get_param('post_id'));
            $subtitle = sanitize_text_field($request->get_param('subtitle'));
            if (!$post_id || !get_post($post_id)) {
                return new WP_Error('invalid_post', 'Post not found', ['status' => 404]);
            }
            update_field('sub_title', $subtitle, $post_id);
            return ['success' => true, 'post_id' => $post_id, 'subtitle' => $subtitle];
        },
        'permission_callback' => function () {
            return current_user_can('edit_posts');
        },
    ]);
});
