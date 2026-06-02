# drivers/spi/spi-mem.c

Subsystem: drivers/spi

## Functions (35)

### devm_spi_mem_dirmap_create
- Return type: spi_mem_dirmap_desc *
- Signature: devm_spi_mem_dirmap_create(struct device * dev,struct spi_mem * mem,const struct spi_mem_dirmap_info * info)
- Line: 789

### devm_spi_mem_dirmap_destroy
- Return type: void
- Signature: devm_spi_mem_dirmap_destroy(struct device * dev,struct spi_mem_dirmap_desc * desc)
- Line: 830

### devm_spi_mem_dirmap_match
- Return type: static int
- Signature: devm_spi_mem_dirmap_match(struct device * dev,void * res,void * data)
- Line: 811

### devm_spi_mem_dirmap_release
- Return type: static void
- Signature: devm_spi_mem_dirmap_release(struct device * dev,void * res)
- Line: 769

### spi_check_buswidth_req
- Return type: static int
- Signature: spi_check_buswidth_req(struct spi_mem * mem,u8 buswidth,bool tx)
- Line: 107

### spi_controller_dma_map_mem_op_data
- Return type: int
- Signature: spi_controller_dma_map_mem_op_data(struct spi_controller * ctlr,const struct spi_mem_op * op,struct sg_table * sgt)
- Line: 39

### spi_controller_dma_unmap_mem_op_data
- Return type: void
- Signature: spi_controller_dma_unmap_mem_op_data(struct spi_controller * ctlr,const struct spi_mem_op * op,struct sg_table * sgt)
- Line: 85

### spi_mem_access_end
- Return type: static void
- Signature: spi_mem_access_end(struct spi_mem * mem)
- Line: 319

### spi_mem_access_start
- Return type: static int
- Signature: spi_mem_access_start(struct spi_mem * mem)
- Line: 292

### spi_mem_add_op_stats
- Return type: static void
- Signature: spi_mem_add_op_stats(struct spi_statistics __percpu * pcpu_stats,const struct spi_mem_op * op,int exec_op_ret)
- Line: 330

### spi_mem_adjust_op_freq
- Return type: void
- Signature: spi_mem_adjust_op_freq(struct spi_mem * mem,struct spi_mem_op * op)
- Line: 588

### spi_mem_adjust_op_size
- Return type: int
- Signature: spi_mem_adjust_op_size(struct spi_mem * mem,struct spi_mem_op * op)
- Line: 552

### spi_mem_buswidth_is_valid
- Return type: static bool
- Signature: spi_mem_buswidth_is_valid(u8 buswidth)
- Line: 218

### spi_mem_calc_op_duration
- Return type: u64
- Signature: spi_mem_calc_op_duration(struct spi_mem * mem,struct spi_mem_op * op)
- Line: 614

### spi_mem_check_buswidth
- Return type: static bool
- Signature: spi_mem_check_buswidth(struct spi_mem * mem,const struct spi_mem_op * op)
- Line: 145

### spi_mem_check_op
- Return type: static int
- Signature: spi_mem_check_op(const struct spi_mem_op * op)
- Line: 226

### spi_mem_default_supports_op
- Return type: bool
- Signature: spi_mem_default_supports_op(struct spi_mem * mem,const struct spi_mem_op * op)
- Line: 167

### spi_mem_dirmap_create
- Return type: spi_mem_dirmap_desc *
- Signature: spi_mem_dirmap_create(struct spi_mem * mem,const struct spi_mem_dirmap_info * info)
- Line: 701

### spi_mem_dirmap_destroy
- Return type: void
- Signature: spi_mem_dirmap_destroy(struct spi_mem_dirmap_desc * desc)
- Line: 758

### spi_mem_dirmap_read
- Return type: ssize_t
- Signature: spi_mem_dirmap_read(struct spi_mem_dirmap_desc * desc,u64 offs,size_t len,void * buf)
- Line: 854

### spi_mem_dirmap_write
- Return type: ssize_t
- Signature: spi_mem_dirmap_write(struct spi_mem_dirmap_desc * desc,u64 offs,size_t len,const void * buf)
- Line: 900

### spi_mem_driver_register_with_owner
- Return type: int
- Signature: spi_mem_driver_register_with_owner(struct spi_mem_driver * memdrv,struct module * owner)
- Line: 1073

### spi_mem_driver_unregister
- Return type: void
- Signature: spi_mem_driver_unregister(struct spi_mem_driver * memdrv)
- Line: 1090

### spi_mem_exec_op
- Return type: int
- Signature: spi_mem_exec_op(struct spi_mem * mem,const struct spi_mem_op * op)
- Line: 385

### spi_mem_get_name
- Return type: const char *
- Signature: spi_mem_get_name(struct spi_mem * mem)
- Line: 531

### spi_mem_internal_supports_op
- Return type: static bool
- Signature: spi_mem_internal_supports_op(struct spi_mem * mem,const struct spi_mem_op * op)
- Line: 254

### spi_mem_no_dirmap_read
- Return type: static ssize_t
- Signature: spi_mem_no_dirmap_read(struct spi_mem_dirmap_desc * desc,u64 offs,size_t len,void * buf)
- Line: 647

### spi_mem_no_dirmap_write
- Return type: static ssize_t
- Signature: spi_mem_no_dirmap_write(struct spi_mem_dirmap_desc * desc,u64 offs,size_t len,const void * buf)
- Line: 667

### spi_mem_poll_status
- Return type: int
- Signature: spi_mem_poll_status(struct spi_mem * mem,const struct spi_mem_op * op,u16 mask,u16 match,unsigned long initial_delay_us,unsigned long polling_delay_us,u16 timeout_ms)
- Line: 970

### spi_mem_probe
- Return type: static int
- Signature: spi_mem_probe(struct spi_device * spi)
- Line: 1020

### spi_mem_read_status
- Return type: static int
- Signature: spi_mem_read_status(struct spi_mem * mem,const struct spi_mem_op * op,u16 * status)
- Line: 935

### spi_mem_remove
- Return type: static void
- Signature: spi_mem_remove(struct spi_device * spi)
- Line: 1045

### spi_mem_shutdown
- Return type: static void
- Signature: spi_mem_shutdown(struct spi_device * spi)
- Line: 1054

### spi_mem_supports_op
- Return type: bool
- Signature: spi_mem_supports_op(struct spi_mem * mem,const struct spi_mem_op * op)
- Line: 280

### to_spi_mem_drv
- Return type: static spi_mem_driver *
- Signature: to_spi_mem_drv(struct device_driver * drv)
- Line: 930

## Macros (2)

- **CREATE_TRACE_POINTS** (line 15)
- **SPI_MEM_MAX_BUSWIDTH** (line 20)
