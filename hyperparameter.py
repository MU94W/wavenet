waveform_bits = 8
waveform_categories = 1 << waveform_bits
waveform_center_cat = 1 << (waveform_bits - 1)
residual_blocks = 2
conv_layers = [8] * residual_blocks
kernel_size = (2, 1)    # use tf.layers.conv2d
dilation_rate_lst_blocks = [[(1 << l, 1) for l in range(c_l)] for c_l in conv_layers]
dilation_channels = 16
skip_dims = 16
dilated_causal_use_bias = False
residual_use_bias = False
skip_use_bias = False

batch_size = 32
split_nums = 32
max_global_steps = 1E5
train_meta_path = './train_meta.pkl'
log_dir = './log'
save_path = './save'