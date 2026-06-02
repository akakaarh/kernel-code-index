# drivers/spi/spi-wpcm-fiu.c

Subsystem: drivers/spi

## Functions (26)

### wpcm_fiu_4ba_exec
- Return type: static int
- Signature: wpcm_fiu_4ba_exec(struct spi_mem * mem,const struct spi_mem_op * op)
- Line: 195

### wpcm_fiu_4ba_match
- Return type: static bool
- Signature: wpcm_fiu_4ba_match(const struct spi_mem_op * op)
- Line: 190

### wpcm_fiu_adjust_op_size
- Return type: static int
- Signature: wpcm_fiu_adjust_op_size(struct spi_mem * mem,struct spi_mem_op * op)
- Line: 367

### wpcm_fiu_direct_read
- Return type: static ssize_t
- Signature: wpcm_fiu_direct_read(struct spi_mem_dirmap_desc * desc,u64 offs,size_t len,void * buf)
- Line: 399

### wpcm_fiu_dirmap_create
- Return type: static int
- Signature: wpcm_fiu_dirmap_create(struct spi_mem_dirmap_desc * desc)
- Line: 375

### wpcm_fiu_do_uma
- Return type: static int
- Signature: wpcm_fiu_do_uma(struct wpcm_fiu_spi * fiu,unsigned int cs,bool use_addr,bool write,int data_bytes)
- Line: 97

### wpcm_fiu_dummy_exec
- Return type: static int
- Signature: wpcm_fiu_dummy_exec(struct spi_mem * mem,const struct spi_mem_op * op)
- Line: 277

### wpcm_fiu_dummy_match
- Return type: static bool
- Signature: wpcm_fiu_dummy_match(const struct spi_mem_op * op)
- Line: 266

### wpcm_fiu_ects_assert
- Return type: static void
- Signature: wpcm_fiu_ects_assert(struct wpcm_fiu_spi * fiu,unsigned int cs)
- Line: 119

### wpcm_fiu_ects_deassert
- Return type: static void
- Signature: wpcm_fiu_ects_deassert(struct wpcm_fiu_spi * fiu,unsigned int cs)
- Line: 127

### wpcm_fiu_exec_op
- Return type: static int
- Signature: wpcm_fiu_exec_op(struct spi_mem * mem,const struct spi_mem_op * op)
- Line: 352

### wpcm_fiu_fast_read_exec
- Return type: static int
- Signature: wpcm_fiu_fast_read_exec(struct spi_mem * mem,const struct spi_mem_op * op)
- Line: 177

### wpcm_fiu_fast_read_match
- Return type: static bool
- Signature: wpcm_fiu_fast_read_match(const struct spi_mem_op * op)
- Line: 169

### wpcm_fiu_find_op_shape
- Return type: static const struct wpcm_fiu_op_shape *
- Signature: wpcm_fiu_find_op_shape(const struct spi_mem_op * op)
- Line: 308

### wpcm_fiu_get_data
- Return type: static void
- Signature: wpcm_fiu_get_data(struct wpcm_fiu_spi * fiu,u8 * data,unsigned int nbytes)
- Line: 86

### wpcm_fiu_hw_init
- Return type: static void
- Signature: wpcm_fiu_hw_init(struct wpcm_fiu_spi * fiu)
- Line: 426

### wpcm_fiu_normal_exec
- Return type: static int
- Signature: wpcm_fiu_normal_exec(struct spi_mem * mem,const struct spi_mem_op * op)
- Line: 150

### wpcm_fiu_normal_match
- Return type: static bool
- Signature: wpcm_fiu_normal_match(const struct spi_mem_op * op)
- Line: 140

### wpcm_fiu_probe
- Return type: static int
- Signature: wpcm_fiu_probe(struct platform_device * pdev)
- Line: 437

### wpcm_fiu_rdid_exec
- Return type: static int
- Signature: wpcm_fiu_rdid_exec(struct spi_mem * mem,const struct spi_mem_op * op)
- Line: 240

### wpcm_fiu_rdid_match
- Return type: static bool
- Signature: wpcm_fiu_rdid_match(const struct spi_mem_op * op)
- Line: 233

### wpcm_fiu_set_addr
- Return type: static void
- Signature: wpcm_fiu_set_addr(struct wpcm_fiu_spi * fiu,u32 addr)
- Line: 71

### wpcm_fiu_set_data
- Return type: static void
- Signature: wpcm_fiu_set_data(struct wpcm_fiu_spi * fiu,const u8 * data,unsigned int nbytes)
- Line: 78

### wpcm_fiu_set_opcode
- Return type: static void
- Signature: wpcm_fiu_set_opcode(struct wpcm_fiu_spi * fiu,u8 opcode)
- Line: 66

### wpcm_fiu_stall_host
- Return type: static void
- Signature: wpcm_fiu_stall_host(struct wpcm_fiu_spi * fiu,bool stall)
- Line: 341

### wpcm_fiu_supports_op
- Return type: static bool
- Signature: wpcm_fiu_supports_op(struct spi_mem * mem,const struct spi_mem_op * op)
- Line: 322

## Structs (2)

### wpcm_fiu_op_shape
- Line: 135
- Members:
  - dev: device *
  - clk: clk *
  - regs: void __iomem *
  - memory: void __iomem *
  - memory_size: size_t
  - shm_regmap: regmap *
  - match: bool (*)(const struct spi_mem_op * op)
  - exec: int (*)(struct spi_mem * mem,const struct spi_mem_op * op)

### wpcm_fiu_spi
- Line: 57
- Members:
  - dev: device *
  - clk: clk *
  - regs: void __iomem *
  - memory: void __iomem *
  - memory_size: size_t
  - shm_regmap: regmap *
  - match: bool (*)(const struct spi_mem_op * op)
  - exec: int (*)(struct spi_mem * mem,const struct spi_mem_op * op)

## Variables (4)

- static **wpcm_fiu_driver** : platform_driver (line 491)
- static **wpcm_fiu_dt_ids** : const struct of_device_id[] (line 485)
- static **wpcm_fiu_mem_ops** : const struct spi_controller_mem_ops (line 418)
- static **wpcm_fiu_op_shapes** : const struct wpcm_fiu_op_shape[] (line 300)

## Macros (34)

- **FIU_BURST_BFG** (line 13)
- **FIU_BURST_CFG_R16** (line 36)
- **FIU_CFBB_PROT** (line 15)
- **FIU_CFG** (line 12)
- **FIU_FWIN1_HIGH** (line 17)
- **FIU_FWIN1_LOW** (line 16)
- **FIU_FWIN2_HIGH** (line 19)
- **FIU_FWIN2_LOW** (line 18)
- **FIU_FWIN3_HIGH** (line 21)
- **FIU_FWIN3_LOW** (line 20)
- **FIU_PROT_CLEAR** (line 23)
- **FIU_PROT_LOCK** (line 22)
- **FIU_RESP_CFG** (line 14)
- **FIU_SPI_FL_CFG** (line 24)
- **FIU_UMA_AB0** (line 26)
- **FIU_UMA_AB1** (line 27)
- **FIU_UMA_AB2** (line 28)
- **FIU_UMA_CODE** (line 25)
- **FIU_UMA_CTS** (line 33)
- **FIU_UMA_CTS_A_SIZE** (line 39)
- **FIU_UMA_CTS_CS**(x) (line 41)
- **FIU_UMA_CTS_D_SIZE**(x) (line 38)
- **FIU_UMA_CTS_EXEC_DONE** (line 42)
- **FIU_UMA_CTS_WR** (line 40)
- **FIU_UMA_DB0** (line 29)
- **FIU_UMA_DB1** (line 30)
- **FIU_UMA_DB2** (line 31)
- **FIU_UMA_DB3** (line 32)
- **FIU_UMA_ECTS** (line 34)
- **MAX_MEMORY_SIZE_PER_CS** (line 54)
- **MAX_MEMORY_SIZE_TOTAL** (line 55)
- **SHM_FLASH_SIZE** (line 44)
- **SHM_FLASH_SIZE_STALL_HOST** (line 45)
- **UMA_WAIT_ITERATIONS** (line 51)
