# drivers/i2c/busses/i2c-virtio.c

Subsystem: drivers/i2c

## Functions (11)

### virtio_i2c_complete_reqs
- Return type: static int
- Signature: virtio_i2c_complete_reqs(struct virtqueue * vq,struct virtio_i2c_req * reqs,struct i2c_msg * msgs,int num)
- Line: 109

### virtio_i2c_del_vqs
- Return type: static void
- Signature: virtio_i2c_del_vqs(struct virtio_device * vdev)
- Line: 167

### virtio_i2c_freeze
- Return type: static int
- Signature: virtio_i2c_freeze(struct virtio_device * vdev)
- Line: 246

### virtio_i2c_func
- Return type: static u32
- Signature: virtio_i2c_func(struct i2c_adapter * adap)
- Line: 181

### virtio_i2c_msg_done
- Return type: static void
- Signature: virtio_i2c_msg_done(struct virtqueue * vq)
- Line: 48

### virtio_i2c_prepare_reqs
- Return type: static int
- Signature: virtio_i2c_prepare_reqs(struct virtqueue * vq,struct virtio_i2c_req * reqs,struct i2c_msg * msgs,int num)
- Line: 57

### virtio_i2c_probe
- Return type: static int
- Signature: virtio_i2c_probe(struct virtio_device * vdev)
- Line: 191

### virtio_i2c_remove
- Return type: static void
- Signature: virtio_i2c_remove(struct virtio_device * vdev)
- Line: 232

### virtio_i2c_restore
- Return type: static int
- Signature: virtio_i2c_restore(struct virtio_device * vdev)
- Line: 252

### virtio_i2c_setup_vqs
- Return type: static int
- Signature: virtio_i2c_setup_vqs(struct virtio_i2c * vi)
- Line: 173

### virtio_i2c_xfer
- Return type: static int
- Signature: virtio_i2c_xfer(struct i2c_adapter * adap,struct i2c_msg * msgs,int num)
- Line: 134

## Structs (2)

### virtio_i2c
- Line: 28
- Members:
  - vdev: virtio_device *
  - adap: i2c_adapter
  - vq: virtqueue *
  - completion: completion
  - ____cacheline_aligned: virtio_i2c_out_hdr out_hdr
  - ____cacheline_aligned: uint8_t * buf
  - ____cacheline_aligned: virtio_i2c_in_hdr in_hdr

### virtio_i2c_req
- Line: 41
- Members:
  - vdev: virtio_device *
  - adap: i2c_adapter
  - vq: virtqueue *
  - completion: completion
  - ____cacheline_aligned: virtio_i2c_out_hdr out_hdr
  - ____cacheline_aligned: uint8_t * buf
  - ____cacheline_aligned: virtio_i2c_in_hdr in_hdr

## Variables (4)

- static **features** : const unsigned int[] (line 257)
- static **id_table** : const struct virtio_device_id[] (line 240)
- static **virtio_algorithm** : const struct i2c_algorithm (line 186)
- static **virtio_i2c_driver** : virtio_driver (line 261)
