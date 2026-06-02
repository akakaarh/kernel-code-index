# drivers/i2c/busses/i2c-imx.c

Subsystem: drivers/i2c

## Functions (52)

### i2c_adap_imx_exit
- Return type: static void __exit
- Signature: i2c_adap_imx_exit(void)
- Line: 1973

### i2c_adap_imx_init
- Return type: static int __init
- Signature: i2c_adap_imx_init(void)
- Line: 1967

### i2c_imx_acked
- Return type: static int
- Signature: i2c_imx_acked(struct imx_i2c_struct * i2c_imx)
- Line: 615

### i2c_imx_atomic_read
- Return type: static int
- Signature: i2c_imx_atomic_read(struct imx_i2c_struct * i2c_imx,struct i2c_msg * msgs,bool is_lastmsg)
- Line: 1412

### i2c_imx_atomic_write
- Return type: static int
- Signature: i2c_imx_atomic_write(struct imx_i2c_struct * i2c_imx,struct i2c_msg * msgs)
- Line: 1348

### i2c_imx_bus_busy
- Return type: static int
- Signature: i2c_imx_bus_busy(struct imx_i2c_struct * i2c_imx,int for_busy,bool atomic)
- Line: 536

### i2c_imx_clear_irq
- Return type: static void
- Signature: i2c_imx_clear_irq(struct imx_i2c_struct * i2c_imx,unsigned int bits)
- Line: 379

### i2c_imx_clk_notifier_call
- Return type: static int
- Signature: i2c_imx_clk_notifier_call(struct notifier_block * nb,unsigned long action,void * data)
- Line: 681

### i2c_imx_dma_callback
- Return type: static void
- Signature: i2c_imx_dma_callback(void * arg)
- Line: 467

### i2c_imx_dma_free
- Return type: static void
- Signature: i2c_imx_dma_free(struct imx_i2c_struct * i2c_imx)
- Line: 520

### i2c_imx_dma_read
- Return type: static int
- Signature: i2c_imx_dma_read(struct imx_i2c_struct * i2c_imx,struct i2c_msg * msgs,bool is_lastmsg)
- Line: 1255

### i2c_imx_dma_request
- Return type: static int
- Signature: i2c_imx_dma_request(struct imx_i2c_struct * i2c_imx,dma_addr_t phy_addr)
- Line: 401

### i2c_imx_dma_write
- Return type: static int
- Signature: i2c_imx_dma_write(struct imx_i2c_struct * i2c_imx,struct i2c_msg * msgs)
- Line: 1155

### i2c_imx_dma_xfer
- Return type: static int
- Signature: i2c_imx_dma_xfer(struct imx_i2c_struct * i2c_imx,struct i2c_msg * msgs)
- Line: 477

### i2c_imx_enable_bus_idle
- Return type: static void
- Signature: i2c_imx_enable_bus_idle(struct imx_i2c_struct * i2c_imx)
- Line: 764

### i2c_imx_func
- Return type: static u32
- Signature: i2c_imx_func(struct i2c_adapter * adapter)
- Line: 1697

### i2c_imx_init_recovery_info
- Return type: static int
- Signature: i2c_imx_init_recovery_info(struct imx_i2c_struct * i2c_imx,struct platform_device * pdev)
- Line: 1683

### i2c_imx_isr
- Return type: static irqreturn_t
- Signature: i2c_imx_isr(int irq,void * dev_id)
- Line: 1129

### i2c_imx_isr_acked
- Return type: static int
- Signature: i2c_imx_isr_acked(struct imx_i2c_struct * i2c_imx)
- Line: 971

### i2c_imx_isr_read
- Return type: static int
- Signature: i2c_imx_isr_read(struct imx_i2c_struct * i2c_imx)
- Line: 1000

### i2c_imx_isr_read_block_data_len
- Return type: static void
- Signature: i2c_imx_isr_read_block_data_len(struct imx_i2c_struct * i2c_imx)
- Line: 1061

### i2c_imx_isr_read_continue
- Return type: static imx_i2c_state
- Signature: i2c_imx_isr_read_continue(struct imx_i2c_struct * i2c_imx)
- Line: 1021

### i2c_imx_isr_write
- Return type: static int
- Signature: i2c_imx_isr_write(struct imx_i2c_struct * i2c_imx)
- Line: 984

### i2c_imx_master_isr
- Return type: static irqreturn_t
- Signature: i2c_imx_master_isr(struct imx_i2c_struct * i2c_imx,unsigned int status)
- Line: 1074

### i2c_imx_prepare_read
- Return type: static int
- Signature: i2c_imx_prepare_read(struct imx_i2c_struct * i2c_imx,struct i2c_msg * msgs,bool use_dma)
- Line: 1219

### i2c_imx_probe
- Return type: static int
- Signature: i2c_imx_probe(struct platform_device * pdev)
- Line: 1711

### i2c_imx_read
- Return type: static int
- Signature: i2c_imx_read(struct imx_i2c_struct * i2c_imx,struct i2c_msg * msgs,bool is_lastmsg)
- Line: 1491

### i2c_imx_reg_slave
- Return type: static int
- Signature: i2c_imx_reg_slave(struct i2c_client * client)
- Line: 925

### i2c_imx_remove
- Return type: static void
- Signature: i2c_imx_remove(struct platform_device * pdev)
- Line: 1859

### i2c_imx_reset_regs
- Return type: static void
- Signature: i2c_imx_reset_regs(struct imx_i2c_struct * i2c_imx)
- Line: 393

### i2c_imx_resume
- Return type: static int
- Signature: i2c_imx_resume(struct device * dev)
- Line: 1941

### i2c_imx_runtime_resume
- Return type: static int
- Signature: i2c_imx_runtime_resume(struct device * dev)
- Line: 1900

### i2c_imx_runtime_suspend
- Return type: static int
- Signature: i2c_imx_runtime_suspend(struct device * dev)
- Line: 1892

### i2c_imx_set_clk
- Return type: static int
- Signature: i2c_imx_set_clk(struct imx_i2c_struct * i2c_imx,unsigned int i2c_clk_rate)
- Line: 626

### i2c_imx_slave_event
- Return type: static void
- Signature: i2c_imx_slave_event(struct imx_i2c_struct * i2c_imx,enum i2c_slave_event event,u8 * val)
- Line: 775

### i2c_imx_slave_finish_op
- Return type: static void
- Signature: i2c_imx_slave_finish_op(struct imx_i2c_struct * i2c_imx)
- Line: 782

### i2c_imx_slave_handle
- Return type: static irqreturn_t
- Signature: i2c_imx_slave_handle(struct imx_i2c_struct * i2c_imx,unsigned int status,unsigned int ctl)
- Line: 806

### i2c_imx_slave_init
- Return type: static void
- Signature: i2c_imx_slave_init(struct imx_i2c_struct * i2c_imx)
- Line: 905

### i2c_imx_slave_timeout
- Return type: static hrtimer_restart
- Signature: i2c_imx_slave_timeout(struct hrtimer * t)
- Line: 890

### i2c_imx_start
- Return type: static int
- Signature: i2c_imx_start(struct imx_i2c_struct * i2c_imx,bool atomic)
- Line: 696

### i2c_imx_stop
- Return type: static void
- Signature: i2c_imx_stop(struct imx_i2c_struct * i2c_imx,bool atomic)
- Line: 729

### i2c_imx_suspend
- Return type: static int
- Signature: i2c_imx_suspend(struct device * dev)
- Line: 1916

### i2c_imx_trx_complete
- Return type: static int
- Signature: i2c_imx_trx_complete(struct imx_i2c_struct * i2c_imx,bool atomic)
- Line: 573

### i2c_imx_unreg_slave
- Return type: static int
- Signature: i2c_imx_unreg_slave(struct i2c_client * client)
- Line: 948

### i2c_imx_write
- Return type: static int
- Signature: i2c_imx_write(struct imx_i2c_struct * i2c_imx,struct i2c_msg * msgs)
- Line: 1382

### i2c_imx_xfer
- Return type: static int
- Signature: i2c_imx_xfer(struct i2c_adapter * adapter,struct i2c_msg * msgs,int num)
- Line: 1642

### i2c_imx_xfer_atomic
- Return type: static int
- Signature: i2c_imx_xfer_atomic(struct i2c_adapter * adapter,struct i2c_msg * msgs,int num)
- Line: 1659

### i2c_imx_xfer_common
- Return type: static int
- Signature: i2c_imx_xfer_common(struct i2c_adapter * adapter,struct i2c_msg * msgs,int num,bool atomic)
- Line: 1544

### imx_i2c_read_reg
- Return type: static unsigned char
- Signature: imx_i2c_read_reg(struct imx_i2c_struct * i2c_imx,unsigned int reg)
- Line: 373

### imx_i2c_write_reg
- Return type: static void
- Signature: imx_i2c_write_reg(unsigned int val,struct imx_i2c_struct * i2c_imx,unsigned int reg)
- Line: 367

### is_imx1_i2c
- Return type: static int
- Signature: is_imx1_i2c(struct imx_i2c_struct * i2c_imx)
- Line: 357

### is_vf610_i2c
- Return type: static int
- Signature: is_vf610_i2c(struct imx_i2c_struct * i2c_imx)
- Line: 362

## Structs (4)

### imx_i2c_clk_pair
- Line: 130
- Members:
  - div: u16
  - val: u16
  - devtype: imx_i2c_type
  - regshift: unsigned int
  - clk_div: imx_i2c_clk_pair *
  - ndivs: unsigned int
  - i2sr_clr_opcode: unsigned int
  - i2cr_ien_opcode: unsigned int
  - has_err007805: bool
  - chan_tx: dma_chan *
  - chan_rx: dma_chan *
  - chan_using: dma_chan *
  - cmd_complete: completion
  - dma_buf: dma_addr_t
  - dma_len: unsigned int
  - dma_transfer_dir: dma_transfer_direction
  - dma_data_dir: dma_data_direction
  - adapter: i2c_adapter
  - clk: clk *
  - clk_change_nb: notifier_block
  - base: void __iomem *
  - queue: wait_queue_head_t
  - i2csr: unsigned long
  - disable_delay: unsigned int
  - stopped: int
  - ifdr: unsigned int
  - cur_clk: unsigned int
  - bitrate: unsigned int
  - hwdata: const struct imx_i2c_hwdata *
  - rinfo: i2c_bus_recovery_info
  - dma: imx_i2c_dma *
  - slave: i2c_client *
  - last_slave_event: i2c_slave_event
  - msg: i2c_msg *
  - msg_buf_idx: unsigned int
  - isr_result: int
  - is_lastmsg: bool
  - state: imx_i2c_state
  - multi_master: bool
  - slave_lock: spinlock_t
  - slave_timer: hrtimer

### imx_i2c_dma
- Line: 216
- Members:
  - div: u16
  - val: u16
  - devtype: imx_i2c_type
  - regshift: unsigned int
  - clk_div: imx_i2c_clk_pair *
  - ndivs: unsigned int
  - i2sr_clr_opcode: unsigned int
  - i2cr_ien_opcode: unsigned int
  - has_err007805: bool
  - chan_tx: dma_chan *
  - chan_rx: dma_chan *
  - chan_using: dma_chan *
  - cmd_complete: completion
  - dma_buf: dma_addr_t
  - dma_len: unsigned int
  - dma_transfer_dir: dma_transfer_direction
  - dma_data_dir: dma_data_direction
  - adapter: i2c_adapter
  - clk: clk *
  - clk_change_nb: notifier_block
  - base: void __iomem *
  - queue: wait_queue_head_t
  - i2csr: unsigned long
  - disable_delay: unsigned int
  - stopped: int
  - ifdr: unsigned int
  - cur_clk: unsigned int
  - bitrate: unsigned int
  - hwdata: const struct imx_i2c_hwdata *
  - rinfo: i2c_bus_recovery_info
  - dma: imx_i2c_dma *
  - slave: i2c_client *
  - last_slave_event: i2c_slave_event
  - msg: i2c_msg *
  - msg_buf_idx: unsigned int
  - isr_result: int
  - is_lastmsg: bool
  - state: imx_i2c_state
  - multi_master: bool
  - slave_lock: spinlock_t
  - slave_timer: hrtimer

### imx_i2c_hwdata
- Line: 201
- Members:
  - div: u16
  - val: u16
  - devtype: imx_i2c_type
  - regshift: unsigned int
  - clk_div: imx_i2c_clk_pair *
  - ndivs: unsigned int
  - i2sr_clr_opcode: unsigned int
  - i2cr_ien_opcode: unsigned int
  - has_err007805: bool
  - chan_tx: dma_chan *
  - chan_rx: dma_chan *
  - chan_using: dma_chan *
  - cmd_complete: completion
  - dma_buf: dma_addr_t
  - dma_len: unsigned int
  - dma_transfer_dir: dma_transfer_direction
  - dma_data_dir: dma_data_direction
  - adapter: i2c_adapter
  - clk: clk *
  - clk_change_nb: notifier_block
  - base: void __iomem *
  - queue: wait_queue_head_t
  - i2csr: unsigned long
  - disable_delay: unsigned int
  - stopped: int
  - ifdr: unsigned int
  - cur_clk: unsigned int
  - bitrate: unsigned int
  - hwdata: const struct imx_i2c_hwdata *
  - rinfo: i2c_bus_recovery_info
  - dma: imx_i2c_dma *
  - slave: i2c_client *
  - last_slave_event: i2c_slave_event
  - msg: i2c_msg *
  - msg_buf_idx: unsigned int
  - isr_result: int
  - is_lastmsg: bool
  - state: imx_i2c_state
  - multi_master: bool
  - slave_lock: spinlock_t
  - slave_timer: hrtimer

### imx_i2c_struct
- Line: 238
- Members:
  - div: u16
  - val: u16
  - devtype: imx_i2c_type
  - regshift: unsigned int
  - clk_div: imx_i2c_clk_pair *
  - ndivs: unsigned int
  - i2sr_clr_opcode: unsigned int
  - i2cr_ien_opcode: unsigned int
  - has_err007805: bool
  - chan_tx: dma_chan *
  - chan_rx: dma_chan *
  - chan_using: dma_chan *
  - cmd_complete: completion
  - dma_buf: dma_addr_t
  - dma_len: unsigned int
  - dma_transfer_dir: dma_transfer_direction
  - dma_data_dir: dma_data_direction
  - adapter: i2c_adapter
  - clk: clk *
  - clk_change_nb: notifier_block
  - base: void __iomem *
  - queue: wait_queue_head_t
  - i2csr: unsigned long
  - disable_delay: unsigned int
  - stopped: int
  - ifdr: unsigned int
  - cur_clk: unsigned int
  - bitrate: unsigned int
  - hwdata: const struct imx_i2c_hwdata *
  - rinfo: i2c_bus_recovery_info
  - dma: imx_i2c_dma *
  - slave: i2c_client *
  - last_slave_event: i2c_slave_event
  - msg: i2c_msg *
  - msg_buf_idx: unsigned int
  - isr_result: int
  - is_lastmsg: bool
  - state: imx_i2c_state
  - multi_master: bool
  - slave_lock: spinlock_t
  - slave_timer: hrtimer

## Enums (2)

### imx_i2c_state
- Line: 227

### imx_i2c_type
- Line: 194

## Variables (14)

- static **i2c_imx_acpi_ids** : const struct acpi_device_id[] (line 351)
- static **i2c_imx_algo** : const struct i2c_algorithm (line 1703)
- static **i2c_imx_driver** : platform_driver (line 1955)
- static **i2c_imx_dt_ids** : const struct of_device_id[] (line 331)
- static **i2c_imx_pm_ops** : const struct dev_pm_ops (line 1948)
- static **imx1_i2c_hwdata** : const struct imx_i2c_hwdata (line 270)
- static **imx21_i2c_hwdata** : const struct imx_i2c_hwdata (line 280)
- static **imx6_i2c_hwdata** : const struct imx_i2c_hwdata (line 290)
- static **imx_i2c_clk_div** : imx_i2c_clk_pair[] (line 135)
- static **imx_i2c_devtype** : const struct platform_device_id[] (line 318)
- static **s32g2_i2c_clk_div** : imx_i2c_clk_pair[] (line 171)
- static **s32g2_i2c_hwdata** : const struct imx_i2c_hwdata (line 309)
- static **vf610_i2c_clk_div** : imx_i2c_clk_pair[] (line 152)
- static **vf610_i2c_hwdata** : imx_i2c_hwdata (line 300)

## Macros (33)

- **DMA_THRESHOLD** (line 64)
- **DMA_TIMEOUT** (line 65)
- **DRIVER_NAME** (line 54)
- **I2CR_DMAEN** (line 98)
- **I2CR_IEN** (line 104)
- **I2CR_IEN_OPCODE_0** (line 117)
- **I2CR_IEN_OPCODE_1** (line 118)
- **I2CR_IIEN** (line 103)
- **I2CR_MSTA** (line 102)
- **I2CR_MTX** (line 101)
- **I2CR_RSTA** (line 99)
- **I2CR_TXAK** (line 100)
- **I2C_IMX_CHECK_DELAY** (line 56)
- **I2C_PM_TIMEOUT** (line 120)
- **I2SR_CLR_OPCODE_W0C** (line 115)
- **I2SR_CLR_OPCODE_W1C** (line 116)
- **I2SR_IAAS** (line 96)
- **I2SR_IAL** (line 94)
- **I2SR_IBB** (line 95)
- **I2SR_ICF** (line 97)
- **I2SR_IIF** (line 92)
- **I2SR_RXAK** (line 91)
- **I2SR_SRW** (line 93)
- **IBIC_BIIE** (line 105)
- **IMX_I2C_I2CR** (line 77)
- **IMX_I2C_I2DR** (line 79)
- **IMX_I2C_I2SR** (line 78)
- **IMX_I2C_IADR** (line 75)
- **IMX_I2C_IBIC** (line 84)
- **IMX_I2C_IFDR** (line 76)
- **IMX_I2C_REGSHIFT** (line 86)
- **S32G_I2C_REGSHIFT** (line 88)
- **VF610_I2C_REGSHIFT** (line 87)
