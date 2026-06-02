# drivers/spi/spi-sh-msiof.c

Subsystem: drivers/spi

## Functions (47)

### copy_bswap32
- Return type: static void
- Signature: copy_bswap32(u32 * dst,const u32 * src,unsigned int words)
- Line: 772

### copy_plain32
- Return type: static void
- Signature: copy_plain32(u32 * dst,const u32 * src,unsigned int words)
- Line: 810

### copy_wswap32
- Return type: static void
- Signature: copy_wswap32(u32 * dst,const u32 * src,unsigned int words)
- Line: 791

### sh_msiof_dma_complete
- Return type: static void
- Signature: sh_msiof_dma_complete(void * arg)
- Line: 641

### sh_msiof_dma_once
- Return type: static int
- Signature: sh_msiof_dma_once(struct sh_msiof_spi_priv * p,const void * tx,void * rx,unsigned int len,unsigned int max_wdlen)
- Line: 646

### sh_msiof_get_delay_bit
- Return type: static u32
- Signature: sh_msiof_get_delay_bit(u32 dtdl_or_syncdl)
- Line: 176

### sh_msiof_modify_ctr_wait
- Return type: static int
- Signature: sh_msiof_modify_ctr_wait(struct sh_msiof_spi_priv * p,u32 clr,u32 set)
- Line: 91

### sh_msiof_prepare_message
- Return type: static int
- Signature: sh_msiof_prepare_message(struct spi_controller * ctlr,struct spi_message * msg)
- Line: 482

### sh_msiof_read
- Return type: static u32
- Signature: sh_msiof_read(struct sh_msiof_spi_priv * p,int reg_offs)
- Line: 66

### sh_msiof_release_dma
- Return type: static void
- Signature: sh_msiof_release_dma(struct sh_msiof_spi_priv * p)
- Line: 1168

### sh_msiof_request_dma
- Return type: static int
- Signature: sh_msiof_request_dma(struct sh_msiof_spi_priv * p)
- Line: 1093

### sh_msiof_request_dma_chan
- Return type: static dma_chan *
- Signature: sh_msiof_request_dma_chan(struct device * dev,enum dma_transfer_direction dir,unsigned int id,dma_addr_t port_addr)
- Line: 1054

### sh_msiof_reset_str
- Return type: static void
- Signature: sh_msiof_reset_str(struct sh_msiof_spi_priv * p)
- Line: 291

### sh_msiof_spi_get_dtdl_and_syncdl
- Return type: static u32
- Signature: sh_msiof_spi_get_dtdl_and_syncdl(struct sh_msiof_spi_priv * p)
- Line: 193

### sh_msiof_spi_irq
- Return type: static irqreturn_t
- Signature: sh_msiof_spi_irq(int irq,void * data)
- Line: 106

### sh_msiof_spi_parse_dt
- Return type: static sh_msiof_spi_info *
- Signature: sh_msiof_spi_parse_dt(struct device * dev)
- Line: 1020

### sh_msiof_spi_parse_dt
- Return type: static sh_msiof_spi_info *
- Signature: sh_msiof_spi_parse_dt(struct device * dev)
- Line: 1048

### sh_msiof_spi_probe
- Return type: static int
- Signature: sh_msiof_spi_probe(struct platform_device * pdev)
- Line: 1185

### sh_msiof_spi_read_fifo_16
- Return type: static void
- Signature: sh_msiof_spi_read_fifo_16(struct sh_msiof_spi_priv * p,void * rx_buf,unsigned int words,unsigned int fs)
- Line: 385

### sh_msiof_spi_read_fifo_16u
- Return type: static void
- Signature: sh_msiof_spi_read_fifo_16u(struct sh_msiof_spi_priv * p,void * rx_buf,unsigned int words,unsigned int fs)
- Line: 396

### sh_msiof_spi_read_fifo_32
- Return type: static void
- Signature: sh_msiof_spi_read_fifo_32(struct sh_msiof_spi_priv * p,void * rx_buf,unsigned int words,unsigned int fs)
- Line: 407

### sh_msiof_spi_read_fifo_32u
- Return type: static void
- Signature: sh_msiof_spi_read_fifo_32u(struct sh_msiof_spi_priv * p,void * rx_buf,unsigned int words,unsigned int fs)
- Line: 418

### sh_msiof_spi_read_fifo_8
- Return type: static void
- Signature: sh_msiof_spi_read_fifo_8(struct sh_msiof_spi_priv * p,void * rx_buf,unsigned int words,unsigned int fs)
- Line: 374

### sh_msiof_spi_read_fifo_s32
- Return type: static void
- Signature: sh_msiof_spi_read_fifo_s32(struct sh_msiof_spi_priv * p,void * rx_buf,unsigned int words,unsigned int fs)
- Line: 429

### sh_msiof_spi_read_fifo_s32u
- Return type: static void
- Signature: sh_msiof_spi_read_fifo_s32u(struct sh_msiof_spi_priv * p,void * rx_buf,unsigned int words,unsigned int fs)
- Line: 440

### sh_msiof_spi_remove
- Return type: static void
- Signature: sh_msiof_spi_remove(struct platform_device * pdev)
- Line: 1308

### sh_msiof_spi_reset_regs
- Return type: static void
- Signature: sh_msiof_spi_reset_regs(struct sh_msiof_spi_priv * p)
- Line: 117

### sh_msiof_spi_resume
- Return type: static int
- Signature: sh_msiof_spi_resume(struct device * dev)
- Line: 1335

### sh_msiof_spi_set_clk_regs
- Return type: static void
- Signature: sh_msiof_spi_set_clk_regs(struct sh_msiof_spi_priv * p,struct spi_transfer * t)
- Line: 130

### sh_msiof_spi_set_mode_regs
- Return type: static void
- Signature: sh_msiof_spi_set_mode_regs(struct sh_msiof_spi_priv * p,const void * tx_buf,void * rx_buf,u32 bits,u32 words1,u32 words2)
- Line: 265

### sh_msiof_spi_set_pin_regs
- Return type: static void
- Signature: sh_msiof_spi_set_pin_regs(struct sh_msiof_spi_priv * p,u32 ss,bool cpol,bool cpha,bool tx_hi_z,bool lsb_first,bool cs_high)
- Line: 219

### sh_msiof_spi_setup
- Return type: static int
- Signature: sh_msiof_spi_setup(struct spi_device * spi)
- Line: 451

### sh_msiof_spi_start
- Return type: static int
- Signature: sh_msiof_spi_start(struct sh_msiof_spi_priv * p,void * rx_buf)
- Line: 504

### sh_msiof_spi_stop
- Return type: static int
- Signature: sh_msiof_spi_stop(struct sh_msiof_spi_priv * p,void * rx_buf)
- Line: 524

### sh_msiof_spi_suspend
- Return type: static int
- Signature: sh_msiof_spi_suspend(struct device * dev)
- Line: 1328

### sh_msiof_spi_txrx_once
- Return type: static int
- Signature: sh_msiof_spi_txrx_once(struct sh_msiof_spi_priv * p,void (* tx_fifo)(struct sh_msiof_spi_priv *,const void *,unsigned int,unsigned int),void (* rx_fifo)(struct sh_msiof_spi_priv *,void *,unsigned int,unsigned int),const void * tx_buf,void * rx_buf,unsigned int words,unsigned int bits)
- Line: 571

### sh_msiof_spi_write_fifo_16
- Return type: static void
- Signature: sh_msiof_spi_write_fifo_16(struct sh_msiof_spi_priv * p,const void * tx_buf,unsigned int words,unsigned int fs)
- Line: 308

### sh_msiof_spi_write_fifo_16u
- Return type: static void
- Signature: sh_msiof_spi_write_fifo_16u(struct sh_msiof_spi_priv * p,const void * tx_buf,unsigned int words,unsigned int fs)
- Line: 319

### sh_msiof_spi_write_fifo_32
- Return type: static void
- Signature: sh_msiof_spi_write_fifo_32(struct sh_msiof_spi_priv * p,const void * tx_buf,unsigned int words,unsigned int fs)
- Line: 330

### sh_msiof_spi_write_fifo_32u
- Return type: static void
- Signature: sh_msiof_spi_write_fifo_32u(struct sh_msiof_spi_priv * p,const void * tx_buf,unsigned int words,unsigned int fs)
- Line: 341

### sh_msiof_spi_write_fifo_8
- Return type: static void
- Signature: sh_msiof_spi_write_fifo_8(struct sh_msiof_spi_priv * p,const void * tx_buf,unsigned int words,unsigned int fs)
- Line: 297

### sh_msiof_spi_write_fifo_s32
- Return type: static void
- Signature: sh_msiof_spi_write_fifo_s32(struct sh_msiof_spi_priv * p,const void * tx_buf,unsigned int words,unsigned int fs)
- Line: 352

### sh_msiof_spi_write_fifo_s32u
- Return type: static void
- Signature: sh_msiof_spi_write_fifo_s32u(struct sh_msiof_spi_priv * p,const void * tx_buf,unsigned int words,unsigned int fs)
- Line: 363

### sh_msiof_target_abort
- Return type: static int
- Signature: sh_msiof_target_abort(struct spi_controller * ctlr)
- Line: 542

### sh_msiof_transfer_one
- Return type: static int
- Signature: sh_msiof_transfer_one(struct spi_controller * ctlr,struct spi_device * spi,struct spi_transfer * t)
- Line: 815

### sh_msiof_wait_for_completion
- Return type: static int
- Signature: sh_msiof_wait_for_completion(struct sh_msiof_spi_priv * p,struct completion * x)
- Line: 552

### sh_msiof_write
- Return type: static void
- Signature: sh_msiof_write(struct sh_msiof_spi_priv * p,int reg_offs,u32 value)
- Line: 77

## Structs (2)

### sh_msiof_chipdata
- Line: 35
- Members:
  - bits_per_word_mask: u32
  - tx_fifo_size: u16
  - rx_fifo_size: u16
  - ctlr_flags: u16
  - min_div_pow: u16
  - flags: u32
  - ctlr: spi_controller *
  - mapbase: void __iomem *
  - clk: clk *
  - pdev: platform_device *
  - info: sh_msiof_spi_info *
  - done: completion
  - done_txdma: completion
  - tx_fifo_size: unsigned int
  - rx_fifo_size: unsigned int
  - min_div_pow: unsigned int
  - tx_dma_page: void *
  - rx_dma_page: void *
  - tx_dma_addr: dma_addr_t
  - rx_dma_addr: dma_addr_t
  - native_cs_inited: bool
  - native_cs_high: bool
  - target_aborted: bool

### sh_msiof_spi_priv
- Line: 44
- Members:
  - bits_per_word_mask: u32
  - tx_fifo_size: u16
  - rx_fifo_size: u16
  - ctlr_flags: u16
  - min_div_pow: u16
  - flags: u32
  - ctlr: spi_controller *
  - mapbase: void __iomem *
  - clk: clk *
  - pdev: platform_device *
  - info: sh_msiof_spi_info *
  - done: completion
  - done_txdma: completion
  - tx_fifo_size: unsigned int
  - rx_fifo_size: unsigned int
  - min_div_pow: unsigned int
  - tx_dma_page: void *
  - rx_dma_page: void *
  - tx_dma_addr: dma_addr_t
  - rx_dma_addr: dma_addr_t
  - native_cs_inited: bool
  - native_cs_high: bool
  - target_aborted: bool

## Variables (8)

- static **rcar_gen2_data** : const struct sh_msiof_chipdata (line 969)
- static **rcar_gen3_data** : const struct sh_msiof_chipdata (line 978)
- static **rcar_gen4_data** : const struct sh_msiof_chipdata (line 987)
- static **rcar_r8a7795_data** : const struct sh_msiof_chipdata (line 996)
- static **sh_data** : const struct sh_msiof_chipdata (line 961)
- static **sh_msiof_match** : const struct of_device_id[]__maybe_unused (line 1006)
- static **sh_msiof_spi_drv** : platform_driver (line 1345)
- static **spi_driver_ids** : const struct platform_device_id[] (line 1322)

## Macros (2)

- **MAX_SS** (line 64)
- **SH_MSIOF_FLAG_FIXED_DTDL_200** (line 33)
