# drivers/spi/spi-offload.c

Subsystem: drivers/spi

## Functions (16)

### devm_spi_offload_alloc
- Return type: spi_offload *
- Signature: devm_spi_offload_alloc(struct device * dev,size_t priv_size)
- Line: 65

### devm_spi_offload_get
- Return type: spi_offload *
- Signature: devm_spi_offload_get(struct device * dev,struct spi_device * spi,const struct spi_offload_config * config)
- Line: 106

### devm_spi_offload_rx_stream_request_dma_chan
- Return type: dma_chan *
- Signature: devm_spi_offload_rx_stream_request_dma_chan(struct device * dev,struct spi_offload * offload)
- Line: 384

### devm_spi_offload_trigger_get
- Return type: spi_offload_trigger *
- Signature: devm_spi_offload_trigger_get(struct device * dev,struct spi_offload * offload,enum spi_offload_trigger_type type)
- Line: 206

### devm_spi_offload_trigger_register
- Return type: int
- Signature: devm_spi_offload_trigger_register(struct device * dev,struct spi_offload_trigger_info * info)
- Line: 429

### devm_spi_offload_tx_stream_request_dma_chan
- Return type: dma_chan *
- Signature: devm_spi_offload_tx_stream_request_dma_chan(struct device * dev,struct spi_offload * offload)
- Line: 352

### spi_offload_put
- Return type: static void
- Signature: spi_offload_put(void * data)
- Line: 86

### spi_offload_release_dma_chan
- Return type: static void
- Signature: spi_offload_release_dma_chan(void * chan)
- Line: 336

### spi_offload_trigger_disable
- Return type: void
- Signature: spi_offload_trigger_disable(struct spi_offload * offload,struct spi_offload_trigger * trigger)
- Line: 320

### spi_offload_trigger_enable
- Return type: int
- Signature: spi_offload_trigger_enable(struct spi_offload * offload,struct spi_offload_trigger * trigger,struct spi_offload_trigger_config * config)
- Line: 280

### spi_offload_trigger_free
- Return type: static void
- Signature: spi_offload_trigger_free(struct kref * ref)
- Line: 141

### spi_offload_trigger_get
- Return type: static spi_offload_trigger *
- Signature: spi_offload_trigger_get(enum spi_offload_trigger_type type,struct fwnode_reference_args * args)
- Line: 163

### spi_offload_trigger_get_priv
- Return type: void *
- Signature: spi_offload_trigger_get_priv(struct spi_offload_trigger * trigger)
- Line: 461

### spi_offload_trigger_put
- Return type: static void
- Signature: spi_offload_trigger_put(void * data)
- Line: 151

### spi_offload_trigger_unregister
- Return type: static void
- Signature: spi_offload_trigger_unregister(void * data)
- Line: 407

### spi_offload_trigger_validate
- Return type: int
- Signature: spi_offload_trigger_validate(struct spi_offload_trigger * trigger,struct spi_offload_trigger_config * config)
- Line: 248

## Structs (2)

### spi_controller_and_offload
- Line: 34
- Members:
  - controller: spi_controller *
  - offload: spi_offload *
  - list: list_head
  - ref: kref
  - fwnode: fwnode_handle *
  - lock: mutex
  - ops: const struct spi_offload_trigger_ops *
  - priv: void *

### spi_offload_trigger
- Line: 39
- Members:
  - controller: spi_controller *
  - offload: spi_offload *
  - list: list_head
  - ref: kref
  - fwnode: fwnode_handle *
  - lock: mutex
  - ops: const struct spi_offload_trigger_ops *
  - priv: void *

## Macros (1)

- **DEFAULT_SYMBOL_NAMESPACE** (line 17)
