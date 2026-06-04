# drivers/mmc/core/sdio_io.c

Subsystem: drivers/mmc

## Functions (28)

### _sdio_align_size
- Return type: static unsigned int
- Signature: _sdio_align_size(unsigned int sz)
- Line: 207

### sdio_align_size
- Return type: unsigned int
- Signature: sdio_align_size(struct sdio_func * func,unsigned int sz)
- Line: 231

### sdio_claim_host
- Return type: void
- Signature: sdio_claim_host(struct sdio_func * func)
- Line: 27

### sdio_disable_func
- Return type: int
- Signature: sdio_disable_func(struct sdio_func * func)
- Line: 110

### sdio_enable_func
- Return type: int
- Signature: sdio_enable_func(struct sdio_func * func)
- Line: 59

### sdio_f0_readb
- Return type: unsigned char
- Signature: sdio_f0_readb(struct sdio_func * func,unsigned int addr,int * err_ret)
- Line: 629

### sdio_f0_writeb
- Return type: void
- Signature: sdio_f0_writeb(struct sdio_func * func,unsigned char b,unsigned int addr,int * err_ret)
- Line: 665

### sdio_get_host_pm_caps
- Return type: mmc_pm_flag_t
- Signature: sdio_get_host_pm_caps(struct sdio_func * func)
- Line: 698

### sdio_io_rw_ext_helper
- Return type: static int
- Signature: sdio_io_rw_ext_helper(struct sdio_func * func,int write,unsigned addr,int incr_addr,u8 * buf,unsigned size)
- Line: 313

### sdio_max_byte_size
- Return type: static unsigned int
- Signature: sdio_max_byte_size(struct sdio_func * func)
- Line: 187

### sdio_memcpy_fromio
- Return type: int
- Signature: sdio_memcpy_fromio(struct sdio_func * func,void * dst,unsigned int addr,int count)
- Line: 466

### sdio_memcpy_toio
- Return type: int
- Signature: sdio_memcpy_toio(struct sdio_func * func,unsigned int addr,void * src,int count)
- Line: 483

### sdio_readb
- Return type: u8
- Signature: sdio_readb(struct sdio_func * func,unsigned int addr,int * err_ret)
- Line: 378

### sdio_readl
- Return type: u32
- Signature: sdio_readl(struct sdio_func * func,unsigned int addr,int * err_ret)
- Line: 582

### sdio_readsb
- Return type: int
- Signature: sdio_readsb(struct sdio_func * func,void * dst,unsigned int addr,int count)
- Line: 500

### sdio_readw
- Return type: u16
- Signature: sdio_readw(struct sdio_func * func,unsigned int addr,int * err_ret)
- Line: 534

### sdio_release_host
- Return type: void
- Signature: sdio_release_host(struct sdio_func * func)
- Line: 43

### sdio_retune_crc_disable
- Return type: void
- Signature: sdio_retune_crc_disable(struct sdio_func * func)
- Line: 757

### sdio_retune_crc_enable
- Return type: void
- Signature: sdio_retune_crc_enable(struct sdio_func * func)
- Line: 769

### sdio_retune_hold_now
- Return type: void
- Signature: sdio_retune_hold_now(struct sdio_func * func)
- Line: 792

### sdio_retune_release
- Return type: void
- Signature: sdio_retune_release(struct sdio_func * func)
- Line: 808

### sdio_set_block_size
- Return type: int
- Signature: sdio_set_block_size(struct sdio_func * func,unsigned blksz)
- Line: 159

### sdio_set_host_pm_flags
- Return type: int
- Signature: sdio_set_host_pm_flags(struct sdio_func * func,mmc_pm_flag_t flags)
- Line: 720

### sdio_writeb
- Return type: void
- Signature: sdio_writeb(struct sdio_func * func,u8 b,unsigned int addr,int * err_ret)
- Line: 410

### sdio_writeb_readb
- Return type: u8
- Signature: sdio_writeb_readb(struct sdio_func * func,u8 write_byte,unsigned int addr,int * err_ret)
- Line: 439

### sdio_writel
- Return type: void
- Signature: sdio_writel(struct sdio_func * func,u32 b,unsigned int addr,int * err_ret)
- Line: 607

### sdio_writesb
- Return type: int
- Signature: sdio_writesb(struct sdio_func * func,unsigned int addr,void * src,int count)
- Line: 517

### sdio_writew
- Return type: void
- Signature: sdio_writew(struct sdio_func * func,u16 b,unsigned int addr,int * err_ret)
- Line: 559
