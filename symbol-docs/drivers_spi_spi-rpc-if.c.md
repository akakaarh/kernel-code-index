# drivers/spi/spi-rpc-if.c

Subsystem: drivers/spi

## Functions (10)

### rpcif_spi_mem_dirmap_create
- Return type: static int
- Signature: rpcif_spi_mem_dirmap_create(struct spi_mem_dirmap_desc * desc)
- Line: 105

### rpcif_spi_mem_dirmap_read
- Return type: static ssize_t
- Signature: rpcif_spi_mem_dirmap_read(struct spi_mem_dirmap_desc * desc,u64 offs,size_t len,void * buf)
- Line: 91

### rpcif_spi_mem_exec_op
- Return type: static int
- Signature: rpcif_spi_mem_exec_op(struct spi_mem * mem,const struct spi_mem_op * op)
- Line: 125

### rpcif_spi_mem_prepare
- Return type: static void
- Signature: rpcif_spi_mem_prepare(struct spi_device * spi_dev,const struct spi_mem_op * spi_op,u64 * offs,size_t * len)
- Line: 19

### rpcif_spi_mem_supports_op
- Return type: static bool
- Signature: rpcif_spi_mem_supports_op(struct spi_mem * mem,const struct spi_mem_op * op)
- Line: 64

### rpcif_spi_probe
- Return type: static int
- Signature: rpcif_spi_probe(struct platform_device * pdev)
- Line: 144

### rpcif_spi_remove
- Return type: static void
- Signature: rpcif_spi_remove(struct platform_device * pdev)
- Line: 190

### rpcif_spi_resume
- Return type: static int
- Signature: rpcif_spi_resume(struct device * dev)
- Line: 206

### rpcif_spi_suspend
- Return type: static int
- Signature: rpcif_spi_suspend(struct device * dev)
- Line: 199

### xspi_spi_mem_dirmap_write
- Return type: static ssize_t
- Signature: xspi_spi_mem_dirmap_write(struct spi_mem_dirmap_desc * desc,u64 offs,size_t len,const void * buf)
- Line: 78

## Variables (3)

- static **rpc_if_spi_id_table** : const struct platform_device_id[] (line 217)
- static **rpcif_spi_driver** : platform_driver (line 223)
- static **rpcif_spi_mem_ops** : const struct spi_controller_mem_ops (line 136)
