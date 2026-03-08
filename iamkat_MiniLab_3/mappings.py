def create_mappings(cs):
    return {
        # Main encoder turn → previous / next track
        'View_Control': dict(
            track_encoder='display_encoder',
        ),

        # Transport
        'Transport': dict(
            play_button='play_button',
            stop_button='stop_button',
            tap_tempo_button='tap_tempo_button',
        ),

        # Record button uses View_Based_Recording so it does the right thing
        # on both audio and MIDI tracks (arms if needed, then records)
        'View_Based_Recording': dict(
            record_button='record_button',
        ),

        # Mixer — arm, faders for selected track
        'Mixer': dict(
            target_track_arm_button='delete_button',
            target_track_volume_control='volume_fader',
            target_track_send_a_control='send_a_fader',
            target_track_send_b_control='send_b_fader',
            target_track_pan_control='pan_fader',
        ),

        # Undo button → cycle monitoring (In → Auto → Off)
        'Monitoring': dict(
            monitor_button='undo_button',
        ),

        # Arp → scene up, Pad → scene down
        'SceneNavigation': dict(
            scene_up_button='arp_button',
            scene_down_button='pad_button',
        ),

        # Rotaries 1-7 → track volumes 1-7; rotary 8 → master volume
        'VolumeControl': dict(
            **{f'rotary_{i}': f'rotary_{i}' for i in range(1, 9)}
        ),

        # Bank B pads → clip launch on tracks 1-8 at selected scene row
        'ClipLaunch': dict(
            **{f'clip_launch_{i}_button': f'clip_launch_{i}_button' for i in range(1, 9)}
        ),

    }
