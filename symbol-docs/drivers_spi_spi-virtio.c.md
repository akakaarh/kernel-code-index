# drivers/spi/spi-virtio.c

Subsystem: drivers/spi

## Functions (9)

### virtio_spi_del_vq
- Return type: static void
- Signature: virtio_spi_del_vq(void * data)
- Line: 324

### virtio_spi_find_vqs
- Return type: static int
- Signature: virtio_spi_find_vqs(struct virtio_spi_priv * priv)
- Line: 312

### virtio_spi_freeze
- Return type: static int
- Signature: virtio_spi_freeze(struct device * dev)
- Line: 369

### virtio_spi_msg_done
- Return type: static void
- Signature: virtio_spi_msg_done(struct virtqueue * vq)
- Line: 40

### virtio_spi_probe
- Return type: static int
- Signature: virtio_spi_probe(struct virtio_device * vdev)
- Line: 332

### virtio_spi_read_config
- Return type: static void
- Signature: virtio_spi_read_config(struct virtio_device * vdev)
- Line: 258

### virtio_spi_restore
- Return type: static int
- Signature: virtio_spi_restore(struct device * dev)
- Line: 385

### virtio_spi_set_delays
- Return type: static int
- Signature: virtio_spi_set_delays(struct spi_transfer_head * th,struct spi_device * spi,struct spi_transfer * xfer)
- Line: 88

### virtio_spi_transfer_one
- Return type: static int
- Signature: virtio_spi_transfer_one(struct spi_controller * ctrl,struct spi_device * spi,struct spi_transfer * xfer)
- Line: 148

## Structs (2)

### virtio_spi_priv
- Line: 29
- Members:
  - completion: completion
  - tx_buf: const u8 *
  - rx_buf: u8 *
  - ____cacheline_aligned: spi_transfer_head transfer_head
  - result: spi_transfer_result
  - vdev: virtio_device *
  - vq: virtqueue *
  - mode_func_supported: u32
  - max_freq_hz: u32

### virtio_spi_req
- Line: 21
- Members:
  - completion: completion
  - tx_buf: const u8 *
  - rx_buf: u8 *
  - ____cacheline_aligned: spi_transfer_head transfer_head
  - result: spi_transfer_result
  - vdev: virtio_device *
  - vq: virtqueue *
  - mode_func_supported: u32
  - max_freq_hz: u32

## Variables (3)

- static **virtio_spi_driver** : virtio_driver (line 415)
- static **virtio_spi_id_table** : virtio_device_id[] (line 404)
- static **virtio_spi_pm_ops** : const struct dev_pm_ops (line 410)

## Macros (1)

- **VIRTIO_SPI_MODE_MASK** (line 18)
