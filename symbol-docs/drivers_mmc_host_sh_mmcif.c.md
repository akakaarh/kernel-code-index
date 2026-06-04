# drivers/mmc/host/sh_mmcif.c

Subsystem: drivers/mmc

## Functions (37)

### sh_mmcif_bitclr
- Return type: static void
- Signature: sh_mmcif_bitclr(struct sh_mmcif_host * host,unsigned int reg,u32 val)
- Line: 263

### sh_mmcif_bitset
- Return type: static void
- Signature: sh_mmcif_bitset(struct sh_mmcif_host * host,unsigned int reg,u32 val)
- Line: 257

### sh_mmcif_clk_setup
- Return type: static void
- Signature: sh_mmcif_clk_setup(struct sh_mmcif_host * host)
- Line: 1032

### sh_mmcif_clock_control
- Return type: static void
- Signature: sh_mmcif_clock_control(struct sh_mmcif_host * host,unsigned int clk)
- Line: 479

### sh_mmcif_data_trans
- Return type: static int
- Signature: sh_mmcif_data_trans(struct sh_mmcif_host * host,struct mmc_request * mrq,u32 opc)
- Line: 923

### sh_mmcif_dma_complete
- Return type: static void
- Signature: sh_mmcif_dma_complete(void * arg)
- Line: 269

### sh_mmcif_dma_slave_config
- Return type: static int
- Signature: sh_mmcif_dma_slave_config(struct sh_mmcif_host * host,struct dma_chan * chan,enum dma_transfer_direction direction)
- Line: 397

### sh_mmcif_end_cmd
- Return type: static bool
- Signature: sh_mmcif_end_cmd(struct sh_mmcif_host * host)
- Line: 1121

### sh_mmcif_error_manage
- Return type: static int
- Signature: sh_mmcif_error_manage(struct sh_mmcif_host * host)
- Line: 554

### sh_mmcif_get_cmd12response
- Return type: static void
- Signature: sh_mmcif_get_cmd12response(struct sh_mmcif_host * host,struct mmc_command * cmd)
- Line: 834

### sh_mmcif_get_response
- Return type: static void
- Signature: sh_mmcif_get_response(struct sh_mmcif_host * host,struct mmc_command * cmd)
- Line: 822

### sh_mmcif_init_ocr
- Return type: static void
- Signature: sh_mmcif_init_ocr(struct sh_mmcif_host * host)
- Line: 1411

### sh_mmcif_intr
- Return type: static irqreturn_t
- Signature: sh_mmcif_intr(int irq,void * dev_id)
- Line: 1322

### sh_mmcif_irqt
- Return type: static irqreturn_t
- Signature: sh_mmcif_irqt(int irq,void * dev_id)
- Line: 1215

### sh_mmcif_mread_block
- Return type: static bool
- Signature: sh_mmcif_mread_block(struct sh_mmcif_host * host)
- Line: 680

### sh_mmcif_multi_read
- Return type: static void
- Signature: sh_mmcif_multi_read(struct sh_mmcif_host * host,struct mmc_request * mrq)
- Line: 654

### sh_mmcif_multi_write
- Return type: static void
- Signature: sh_mmcif_multi_write(struct sh_mmcif_host * host,struct mmc_request * mrq)
- Line: 764

### sh_mmcif_mwrite_block
- Return type: static bool
- Signature: sh_mmcif_mwrite_block(struct sh_mmcif_host * host)
- Line: 790

### sh_mmcif_probe
- Return type: static int
- Signature: sh_mmcif_probe(struct platform_device * pdev)
- Line: 1428

### sh_mmcif_read_block
- Return type: static bool
- Signature: sh_mmcif_read_block(struct sh_mmcif_host * host)
- Line: 619

### sh_mmcif_release_dma
- Return type: static void
- Signature: sh_mmcif_release_dma(struct sh_mmcif_host * host)
- Line: 461

### sh_mmcif_remove
- Return type: static void
- Signature: sh_mmcif_remove(struct platform_device * pdev)
- Line: 1546

### sh_mmcif_request
- Return type: static void
- Signature: sh_mmcif_request(struct mmc_host * mmc,struct mmc_request * mrq)
- Line: 1008

### sh_mmcif_request_dma
- Return type: static void
- Signature: sh_mmcif_request_dma(struct sh_mmcif_host * host)
- Line: 421

### sh_mmcif_request_dma_pdata
- Return type: static dma_chan *
- Signature: sh_mmcif_request_dma_pdata(struct sh_mmcif_host * host,uintptr_t slave_id)
- Line: 385

### sh_mmcif_set_cmd
- Return type: static u32
- Signature: sh_mmcif_set_cmd(struct sh_mmcif_host * host,struct mmc_request * mrq)
- Line: 840

### sh_mmcif_set_ios
- Return type: static void
- Signature: sh_mmcif_set_ios(struct mmc_host * mmc,struct mmc_ios * ios)
- Line: 1065

### sh_mmcif_single_read
- Return type: static void
- Signature: sh_mmcif_single_read(struct sh_mmcif_host * host,struct mmc_request * mrq)
- Line: 602

### sh_mmcif_single_write
- Return type: static void
- Signature: sh_mmcif_single_write(struct sh_mmcif_host * host,struct mmc_request * mrq)
- Line: 712

### sh_mmcif_start_cmd
- Return type: static void
- Signature: sh_mmcif_start_cmd(struct sh_mmcif_host * host,struct mmc_request * mrq)
- Line: 948

### sh_mmcif_start_dma_rx
- Return type: static void
- Signature: sh_mmcif_start_dma_rx(struct sh_mmcif_host * host)
- Line: 284

### sh_mmcif_start_dma_tx
- Return type: static void
- Signature: sh_mmcif_start_dma_tx(struct sh_mmcif_host * host)
- Line: 334

### sh_mmcif_stop_cmd
- Return type: static void
- Signature: sh_mmcif_stop_cmd(struct sh_mmcif_host * host,struct mmc_request * mrq)
- Line: 987

### sh_mmcif_suspend
- Return type: static int
- Signature: sh_mmcif_suspend(struct device * dev)
- Line: 1571

### sh_mmcif_sync_reset
- Return type: static void
- Signature: sh_mmcif_sync_reset(struct sh_mmcif_host * host)
- Line: 536

### sh_mmcif_timeout_work
- Return type: static void
- Signature: sh_mmcif_timeout_work(struct work_struct * work)
- Line: 1358

### sh_mmcif_write_block
- Return type: static bool
- Signature: sh_mmcif_write_block(struct sh_mmcif_host * host)
- Line: 729

## Structs (1)

### sh_mmcif_host
- Line: 219
- Members:
  - mmc: mmc_host *
  - mrq: mmc_request *
  - pd: platform_device *
  - clk: clk *
  - bus_width: int
  - timing: unsigned char
  - sd_error: bool
  - dying: bool
  - timeout: long
  - addr: void __iomem *
  - lock: spinlock_t
  - state: sh_mmcif_state
  - wait_for: sh_mmcif_wait_for
  - timeout_work: delayed_work
  - blocksize: size_t
  - sg_miter: sg_mapping_iter
  - power: bool
  - ccs_enable: bool
  - clk_ctrl2_enable: bool
  - thread_lock: mutex
  - clkdiv_map: u32
  - chan_rx: dma_chan *
  - chan_tx: dma_chan *
  - dma_complete: completion
  - dma_active: bool

## Enums (2)

### sh_mmcif_state
- Line: 197

### sh_mmcif_wait_for
- Line: 204

## Variables (3)

- static **sh_mmcif_driver** : platform_driver (line 1584)
- static **sh_mmcif_of_match** : const struct of_device_id[] (line 249)
- static **sh_mmcif_ops** : const struct mmc_host_ops (line 1115)

## Macros (105)

- **BLOCK_SIZE_MASK** (line 91)
- **CLKDEV_EMMC_DATA** (line 193)
- **CLKDEV_INIT** (line 195)
- **CLKDEV_MMC_DATA** (line 194)
- **CMD_CTRL_BREAK** (line 88)
- **CMD_MASK** (line 61)
- **CMD_SET_CCSEN** (line 66)
- **CMD_SET_CCSH** (line 81)
- **CMD_SET_CMD12EN** (line 70)
- **CMD_SET_CMLTE** (line 69)
- **CMD_SET_CRC16C** (line 77)
- **CMD_SET_CRC7C** (line 74)
- **CMD_SET_CRC7C_BITS** (line 75)
- **CMD_SET_CRC7C_INTERNAL** (line 76)
- **CMD_SET_CRCSTE** (line 78)
- **CMD_SET_DARS** (line 82)
- **CMD_SET_DATW_1** (line 83)
- **CMD_SET_DATW_4** (line 84)
- **CMD_SET_DATW_8** (line 85)
- **CMD_SET_DWEN** (line 68)
- **CMD_SET_OPDM** (line 80)
- **CMD_SET_RBSY** (line 65)
- **CMD_SET_RIDXC_BITS** (line 72)
- **CMD_SET_RIDXC_INDEX** (line 71)
- **CMD_SET_RIDXC_NO** (line 73)
- **CMD_SET_RTYP_17B** (line 64)
- **CMD_SET_RTYP_6B** (line 63)
- **CMD_SET_RTYP_NO** (line 62)
- **CMD_SET_TBIT** (line 79)
- **CMD_SET_WDAT** (line 67)
- **DRIVER_NAME** (line 58)
- **INT_ALL** (line 122)
- **INT_BUFRE** (line 99)
- **INT_BUFREN** (line 101)
- **INT_BUFVIO** (line 106)
- **INT_BUFWEN** (line 100)
- **INT_CCS** (line 126)
- **INT_CCSDE** (line 94)
- **INT_CCSRCV** (line 102)
- **INT_CCSTO** (line 111)
- **INT_CMD12CRE** (line 97)
- **INT_CMD12DRE** (line 95)
- **INT_CMD12RBE** (line 96)
- **INT_CMDVIO** (line 105)
- **INT_CRCSTO** (line 112)
- **INT_CRSPE** (line 104)
- **INT_DTRANE** (line 98)
- **INT_ERR_STS** (line 117)
- **INT_RBSYE** (line 103)
- **INT_RBSYTO** (line 115)
- **INT_RDATERR** (line 108)
- **INT_RDATTO** (line 114)
- **INT_RIDXERR** (line 109)
- **INT_RSPERR** (line 110)
- **INT_RSPTO** (line 116)
- **INT_WDATERR** (line 107)
- **INT_WDATTO** (line 113)
- **MASK_ALL** (line 129)
- **MASK_CLEAN** (line 159)
- **MASK_MBUFRE** (line 135)
- **MASK_MBUFREN** (line 137)
- **MASK_MBUFVIO** (line 142)
- **MASK_MBUFWEN** (line 136)
- **MASK_MCCSDE** (line 130)
- **MASK_MCCSRCV** (line 138)
- **MASK_MCCSTO** (line 147)
- **MASK_MCMD12CRE** (line 133)
- **MASK_MCMD12DRE** (line 131)
- **MASK_MCMD12RBE** (line 132)
- **MASK_MCMDVIO** (line 141)
- **MASK_MCRCSTO** (line 148)
- **MASK_MCRSPE** (line 140)
- **MASK_MDTRANE** (line 134)
- **MASK_MRBSYE** (line 139)
- **MASK_MRBSYTO** (line 151)
- **MASK_MRDATERR** (line 144)
- **MASK_MRDATTO** (line 150)
- **MASK_MRIDXERR** (line 145)
- **MASK_MRSPERR** (line 146)
- **MASK_MRSPTO** (line 152)
- **MASK_MWDATERR** (line 143)
- **MASK_MWDATTO** (line 149)
- **MASK_START_CMD** (line 154)
- **STS1_CMDSEQ** (line 165)
- **STS2_AC12BSYTO** (line 182)
- **STS2_AC12CRCE** (line 170)
- **STS2_AC12IDXE** (line 176)
- **STS2_AC12REBE** (line 174)
- **STS2_AC12RSPTO** (line 184)
- **STS2_CCSTO** (line 178)
- **STS2_CRC16E** (line 169)
- **STS2_CRCSTE** (line 168)
- **STS2_CRCSTEBE** (line 172)
- **STS2_CRCSTTO** (line 181)
- **STS2_CRC_ERR** (line 186)
- **STS2_DATBSYTO** (line 180)
- **STS2_RDATEBE** (line 173)
- **STS2_RDATTO** (line 179)
- **STS2_RSPBSYTO** (line 183)
- **STS2_RSPCRC7E** (line 171)
- **STS2_RSPEBE** (line 175)
- **STS2_RSPIDXE** (line 177)
- **STS2_RSPTO** (line 185)
- **STS2_TIMEOUT_ERR** (line 188)
- **sh_mmcif_host_to_dev**(host) (line 255)
