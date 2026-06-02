# drivers/spi/spi-npcm-fiu.c

Subsystem: drivers/spi

## Functions (13)

### npcm_fiu_direct_read
- Return type: static ssize_t
- Signature: npcm_fiu_direct_read(struct spi_mem_dirmap_desc * desc,u64 offs,size_t len,void * buf)
- Line: 287

### npcm_fiu_direct_write
- Return type: static ssize_t
- Signature: npcm_fiu_direct_write(struct spi_mem_dirmap_desc * desc,u64 offs,size_t len,const void * buf)
- Line: 314

### npcm_fiu_dirmap_create
- Return type: static int
- Signature: npcm_fiu_dirmap_create(struct spi_mem_dirmap_desc * desc)
- Line: 598

### npcm_fiu_exec_op
- Return type: static int
- Signature: npcm_fiu_exec_op(struct spi_mem * mem,const struct spi_mem_op * op)
- Line: 543

### npcm_fiu_manualwrite
- Return type: static int
- Signature: npcm_fiu_manualwrite(struct spi_mem * mem,const struct spi_mem_op * op)
- Line: 440

### npcm_fiu_probe
- Return type: static int
- Signature: npcm_fiu_probe(struct platform_device * pdev)
- Line: 689

### npcm_fiu_read
- Return type: static int
- Signature: npcm_fiu_read(struct spi_mem * mem,const struct spi_mem_op * op)
- Line: 489

### npcm_fiu_set_drd
- Return type: static void
- Signature: npcm_fiu_set_drd(struct npcm_fiu_spi * fiu,const struct spi_mem_op * op)
- Line: 266

### npcm_fiu_setup
- Return type: static int
- Signature: npcm_fiu_setup(struct spi_device * spi)
- Line: 660

### npcm_fiu_uma_read
- Return type: static int
- Signature: npcm_fiu_uma_read(struct spi_mem * mem,const struct spi_mem_op * op,u32 addr,bool is_address_size,u8 * data,u32 data_size)
- Line: 334

### npcm_fiu_uma_write
- Return type: static int
- Signature: npcm_fiu_uma_write(struct spi_mem * mem,const struct spi_mem_op * op,u8 cmd,bool is_address_size,u8 * data,u32 data_size)
- Line: 390

### npcm_fiux_set_direct_rd
- Return type: static void
- Signature: npcm_fiux_set_direct_rd(struct npcm_fiu_spi * fiu)
- Line: 529

### npcm_fiux_set_direct_wr
- Return type: static void
- Signature: npcm_fiux_set_direct_wr(struct npcm_fiu_spi * fiu)
- Line: 517

## Structs (4)

### fiu_data
- Line: 205
- Members:
  - name: char *
  - fiu_id: u32
  - max_map_size: u32
  - max_cs: u32
  - npcm_fiu_data_info: const struct npcm_fiu_info *
  - fiu_max: int
  - flash_region_mapped_ptr: void __iomem *
  - fiu: npcm_fiu_spi *
  - clkrate: unsigned long
  - chipselect: u32
  - chip: npcm_fiu_chip[]
  - info: const struct npcm_fiu_info *
  - drd_op: spi_mem_op
  - res_mem: resource *
  - regmap: regmap *
  - clkrate: unsigned long
  - dev: device *
  - clk: clk *
  - spix_mode: bool

### npcm_fiu_chip
- Line: 240
- Members:
  - name: char *
  - fiu_id: u32
  - max_map_size: u32
  - max_cs: u32
  - npcm_fiu_data_info: const struct npcm_fiu_info *
  - fiu_max: int
  - flash_region_mapped_ptr: void __iomem *
  - fiu: npcm_fiu_spi *
  - clkrate: unsigned long
  - chipselect: u32
  - chip: npcm_fiu_chip[]
  - info: const struct npcm_fiu_info *
  - drd_op: spi_mem_op
  - res_mem: resource *
  - regmap: regmap *
  - clkrate: unsigned long
  - dev: device *
  - clk: clk *
  - spix_mode: bool

### npcm_fiu_info
- Line: 198
- Members:
  - name: char *
  - fiu_id: u32
  - max_map_size: u32
  - max_cs: u32
  - npcm_fiu_data_info: const struct npcm_fiu_info *
  - fiu_max: int
  - flash_region_mapped_ptr: void __iomem *
  - fiu: npcm_fiu_spi *
  - clkrate: unsigned long
  - chipselect: u32
  - chip: npcm_fiu_chip[]
  - info: const struct npcm_fiu_info *
  - drd_op: spi_mem_op
  - res_mem: resource *
  - regmap: regmap *
  - clkrate: unsigned long
  - dev: device *
  - clk: clk *
  - spix_mode: bool

### npcm_fiu_spi
- Line: 247
- Members:
  - name: char *
  - fiu_id: u32
  - max_map_size: u32
  - max_cs: u32
  - npcm_fiu_data_info: const struct npcm_fiu_info *
  - fiu_max: int
  - flash_region_mapped_ptr: void __iomem *
  - fiu: npcm_fiu_spi *
  - clkrate: unsigned long
  - chipselect: u32
  - chip: npcm_fiu_chip[]
  - info: const struct npcm_fiu_info *
  - drd_op: spi_mem_op
  - res_mem: resource *
  - regmap: regmap *
  - clkrate: unsigned long
  - dev: device *
  - clk: clk *
  - spix_mode: bool

## Enums (4)

### __anon291577610103
- Line: 160

### __anon291577610203
- Line: 167

### __anon291577610303
- Line: 173

### __anon291577610403
- Line: 191

## Variables (8)

- static **npcm7xx_fiu_data** : const struct fiu_data (line 218)
- static **npcm7xx_fiu_info** : const struct npcm_fiu_info[] (line 210)
- static **npcm_fiu_driver** : platform_driver (line 752)
- static **npcm_fiu_dt_ids** : const struct of_device_id[] (line 683)
- static **npcm_fiu_mem_ops** : const struct spi_controller_mem_ops (line 676)
- static **npcm_mtd_regmap_config** : const struct regmap_config (line 259)
- static **npxm8xx_fiu_data** : const struct fiu_data (line 233)
- static **npxm8xx_fiu_info** : const struct npcm_fiu_info[] (line 223)

## Macros (114)

- **CHUNK_SIZE** (line 188)
- **FIU_DRD_MAX_DUMMY_NUMBER** (line 186)
- **MAP_SIZE_128MB** (line 182)
- **MAP_SIZE_16MB** (line 183)
- **MAP_SIZE_8MB** (line 184)
- **NPCM7XX_INTCR3_FIU_FIX** (line 22)
- **NPCM7XX_INTCR3_OFFSET** (line 21)
- **NPCM_FIU_CFG** (line 40)
- **NPCM_FIU_CFG_FIU_FIX** (line 157)
- **NPCM_FIU_DRD_16_BYTE_BURST** (line 179)
- **NPCM_FIU_DRD_ACCTYPE_SHIFT** (line 52)
- **NPCM_FIU_DRD_ADDSIZ_SHIFT** (line 50)
- **NPCM_FIU_DRD_CFG** (line 25)
- **NPCM_FIU_DRD_CFG_ACCTYPE** (line 48)
- **NPCM_FIU_DRD_CFG_ADDSIZ** (line 46)
- **NPCM_FIU_DRD_CFG_DBW** (line 47)
- **NPCM_FIU_DRD_CFG_LCK** (line 44)
- **NPCM_FIU_DRD_CFG_RDCMD** (line 49)
- **NPCM_FIU_DRD_CFG_R_BURST** (line 45)
- **NPCM_FIU_DRD_DBW_SHIFT** (line 51)
- **NPCM_FIU_DWR_16_BYTE_BURST** (line 180)
- **NPCM_FIU_DWR_ABPCK_SHIFT** (line 62)
- **NPCM_FIU_DWR_ADDSIZ_SHIFT** (line 61)
- **NPCM_FIU_DWR_CFG** (line 26)
- **NPCM_FIU_DWR_CFG_ABPCK** (line 58)
- **NPCM_FIU_DWR_CFG_ADDSIZ** (line 57)
- **NPCM_FIU_DWR_CFG_DBPCK** (line 59)
- **NPCM_FIU_DWR_CFG_LCK** (line 55)
- **NPCM_FIU_DWR_CFG_WRCMD** (line 60)
- **NPCM_FIU_DWR_CFG_W_BURST** (line 56)
- **NPCM_FIU_DWR_DBPCK_SHIFT** (line 63)
- **NPCM_FIU_MAX_REG_LIMIT** (line 41)
- **NPCM_FIU_PRT_CFG** (line 31)
- **NPCM_FIU_UMA_ADDR** (line 30)
- **NPCM_FIU_UMA_ADDR_AB0** (line 106)
- **NPCM_FIU_UMA_ADDR_AB1** (line 105)
- **NPCM_FIU_UMA_ADDR_AB2** (line 104)
- **NPCM_FIU_UMA_ADDR_AB3** (line 103)
- **NPCM_FIU_UMA_ADDR_UMA_ADDR** (line 102)
- **NPCM_FIU_UMA_CFG** (line 27)
- **NPCM_FIU_UMA_CFG_ADBPCK** (line 76)
- **NPCM_FIU_UMA_CFG_ADBPCK_SHIFT** (line 78)
- **NPCM_FIU_UMA_CFG_ADDSIZ** (line 71)
- **NPCM_FIU_UMA_CFG_ADDSIZ_SHIFT** (line 82)
- **NPCM_FIU_UMA_CFG_CMBPCK** (line 77)
- **NPCM_FIU_UMA_CFG_CMDSIZ** (line 72)
- **NPCM_FIU_UMA_CFG_CMMLCK** (line 67)
- **NPCM_FIU_UMA_CFG_DBPCK** (line 74)
- **NPCM_FIU_UMA_CFG_DBPCK_SHIFT** (line 80)
- **NPCM_FIU_UMA_CFG_DBSIZ** (line 69)
- **NPCM_FIU_UMA_CFG_DBSIZ_SHIFT** (line 84)
- **NPCM_FIU_UMA_CFG_LCK** (line 66)
- **NPCM_FIU_UMA_CFG_RDATSIZ** (line 68)
- **NPCM_FIU_UMA_CFG_RDATSIZ_SHIFT** (line 85)
- **NPCM_FIU_UMA_CFG_RDBPCK** (line 73)
- **NPCM_FIU_UMA_CFG_RDBPCK_SHIFT** (line 81)
- **NPCM_FIU_UMA_CFG_WDATSIZ** (line 70)
- **NPCM_FIU_UMA_CFG_WDATSIZ_SHIFT** (line 83)
- **NPCM_FIU_UMA_CFG_WDBPCK** (line 75)
- **NPCM_FIU_UMA_CFG_WDBPCK_SHIFT** (line 79)
- **NPCM_FIU_UMA_CMD** (line 29)
- **NPCM_FIU_UMA_CMD_CMD** (line 99)
- **NPCM_FIU_UMA_CMD_DUM1** (line 98)
- **NPCM_FIU_UMA_CMD_DUM2** (line 97)
- **NPCM_FIU_UMA_CMD_DUM3** (line 96)
- **NPCM_FIU_UMA_CTS** (line 28)
- **NPCM_FIU_UMA_CTS_DEV_NUM** (line 91)
- **NPCM_FIU_UMA_CTS_DEV_NUM_SHIFT** (line 93)
- **NPCM_FIU_UMA_CTS_EXEC_DONE** (line 92)
- **NPCM_FIU_UMA_CTS_RDYIE** (line 88)
- **NPCM_FIU_UMA_CTS_RDYST** (line 89)
- **NPCM_FIU_UMA_CTS_SW_CS** (line 90)
- **NPCM_FIU_UMA_DR0** (line 36)
- **NPCM_FIU_UMA_DR0_RB0** (line 136)
- **NPCM_FIU_UMA_DR0_RB1** (line 135)
- **NPCM_FIU_UMA_DR0_RB2** (line 134)
- **NPCM_FIU_UMA_DR0_RB3** (line 133)
- **NPCM_FIU_UMA_DR1** (line 37)
- **NPCM_FIU_UMA_DR1_RB12** (line 142)
- **NPCM_FIU_UMA_DR1_RB13** (line 141)
- **NPCM_FIU_UMA_DR1_RB14** (line 140)
- **NPCM_FIU_UMA_DR1_RB15** (line 139)
- **NPCM_FIU_UMA_DR2** (line 38)
- **NPCM_FIU_UMA_DR2_RB12** (line 148)
- **NPCM_FIU_UMA_DR2_RB13** (line 147)
- **NPCM_FIU_UMA_DR2_RB14** (line 146)
- **NPCM_FIU_UMA_DR2_RB15** (line 145)
- **NPCM_FIU_UMA_DR3** (line 39)
- **NPCM_FIU_UMA_DR3_RB12** (line 154)
- **NPCM_FIU_UMA_DR3_RB13** (line 153)
- **NPCM_FIU_UMA_DR3_RB14** (line 152)
- **NPCM_FIU_UMA_DR3_RB15** (line 151)
- **NPCM_FIU_UMA_DW0** (line 32)
- **NPCM_FIU_UMA_DW0_WB0** (line 112)
- **NPCM_FIU_UMA_DW0_WB1** (line 111)
- **NPCM_FIU_UMA_DW0_WB2** (line 110)
- **NPCM_FIU_UMA_DW0_WB3** (line 109)
- **NPCM_FIU_UMA_DW1** (line 33)
- **NPCM_FIU_UMA_DW1_WB4** (line 118)
- **NPCM_FIU_UMA_DW1_WB5** (line 117)
- **NPCM_FIU_UMA_DW1_WB6** (line 116)
- **NPCM_FIU_UMA_DW1_WB7** (line 115)
- **NPCM_FIU_UMA_DW2** (line 34)
- **NPCM_FIU_UMA_DW2_WB10** (line 122)
- **NPCM_FIU_UMA_DW2_WB11** (line 121)
- **NPCM_FIU_UMA_DW2_WB8** (line 124)
- **NPCM_FIU_UMA_DW2_WB9** (line 123)
- **NPCM_FIU_UMA_DW3** (line 35)
- **NPCM_FIU_UMA_DW3_WB12** (line 130)
- **NPCM_FIU_UMA_DW3_WB13** (line 129)
- **NPCM_FIU_UMA_DW3_WB14** (line 128)
- **NPCM_FIU_UMA_DW3_WB15** (line 127)
- **NPCM_MAX_CHIP_NUM** (line 187)
- **UMA_MICRO_SEC_TIMEOUT** (line 189)
