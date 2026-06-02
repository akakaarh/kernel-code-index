# drivers/spi/spi-intel.c

Subsystem: drivers/spi

## Functions (33)

### intel_spi_adjust_op_size
- Return type: static int
- Signature: intel_spi_adjust_op_size(struct spi_mem * mem,struct spi_mem_op * op)
- Line: 713

### intel_spi_bios_locked_show
- Return type: static ssize_t
- Signature: intel_spi_bios_locked_show(struct device * dev,struct device_attribute * attr,char * buf)
- Line: 1454

### intel_spi_chip_addr
- Return type: static u32
- Signature: intel_spi_chip_addr(const struct intel_spi * ispi,const struct spi_mem * mem)
- Line: 458

### intel_spi_cmp_mem_op
- Return type: static bool
- Signature: intel_spi_cmp_mem_op(const struct intel_spi_mem_op * iop,const struct spi_mem_op * op)
- Line: 719

### intel_spi_dirmap_create
- Return type: static int
- Signature: intel_spi_dirmap_create(struct spi_mem_dirmap_desc * desc)
- Line: 812

### intel_spi_dirmap_read
- Return type: static ssize_t
- Signature: intel_spi_dirmap_read(struct spi_mem_dirmap_desc * desc,u64 offs,size_t len,void * buf)
- Line: 825

### intel_spi_dirmap_write
- Return type: static ssize_t
- Signature: intel_spi_dirmap_write(struct spi_mem_dirmap_desc * desc,u64 offs,size_t len,const void * buf)
- Line: 842

### intel_spi_dump_regs
- Return type: static void
- Signature: intel_spi_dump_regs(struct intel_spi * ispi)
- Line: 199

### intel_spi_erase
- Return type: static int
- Signature: intel_spi_erase(struct intel_spi * ispi,const struct spi_mem * mem,const struct intel_spi_mem_op * iop,const struct spi_mem_op * op)
- Line: 675

### intel_spi_exec_mem_op
- Return type: static int
- Signature: intel_spi_exec_mem_op(struct spi_mem * mem,const struct spi_mem_op * op)
- Line: 789

### intel_spi_fill_partition
- Return type: static void
- Signature: intel_spi_fill_partition(struct intel_spi * ispi,struct mtd_partition * part)
- Line: 1230

### intel_spi_get_name
- Return type: static const char *
- Signature: intel_spi_get_name(struct spi_mem * mem)
- Line: 801

### intel_spi_hw_cycle
- Return type: static int
- Signature: intel_spi_hw_cycle(struct intel_spi * ispi,const struct intel_spi_mem_op * iop,size_t len)
- Line: 366

### intel_spi_init
- Return type: static int
- Signature: intel_spi_init(struct intel_spi * ispi)
- Line: 1079

### intel_spi_is_protected
- Return type: static bool
- Signature: intel_spi_is_protected(const struct intel_spi * ispi,unsigned int base,unsigned int limit)
- Line: 1204

### intel_spi_locked_show
- Return type: static ssize_t
- Signature: intel_spi_locked_show(struct device * dev,struct device_attribute * attr,char * buf)
- Line: 1445

### intel_spi_match_mem_op
- Return type: static const struct intel_spi_mem_op *
- Signature: intel_spi_match_mem_op(struct intel_spi * ispi,const struct spi_mem_op * op)
- Line: 744

### intel_spi_opcode_index
- Return type: static int
- Signature: intel_spi_opcode_index(struct intel_spi * ispi,u8 opcode,int optype)
- Line: 345

### intel_spi_populate_chip
- Return type: static int
- Signature: intel_spi_populate_chip(struct intel_spi * ispi)
- Line: 1375

### intel_spi_probe
- Return type: int
- Signature: intel_spi_probe(struct device * dev,void __iomem * base,const struct intel_spi_boardinfo * info)
- Line: 1489

### intel_spi_protected_show
- Return type: static ssize_t
- Signature: intel_spi_protected_show(struct device * dev,struct device_attribute * attr,char * buf)
- Line: 1436

### intel_spi_read
- Return type: static int
- Signature: intel_spi_read(struct intel_spi * ispi,const struct spi_mem * mem,const struct intel_spi_mem_op * iop,const struct spi_mem_op * op)
- Line: 551

### intel_spi_read_block
- Return type: static int
- Signature: intel_spi_read_block(struct intel_spi * ispi,void * buf,size_t size)
- Line: 279

### intel_spi_read_desc
- Return type: static int
- Signature: intel_spi_read_desc(struct intel_spi * ispi)
- Line: 1283

### intel_spi_read_reg
- Return type: static int
- Signature: intel_spi_read_reg(struct intel_spi * ispi,const struct spi_mem * mem,const struct intel_spi_mem_op * iop,const struct spi_mem_op * op)
- Line: 467

### intel_spi_set_writeable
- Return type: static bool
- Signature: intel_spi_set_writeable(struct intel_spi * ispi)
- Line: 337

### intel_spi_supports_mem_op
- Return type: static bool
- Signature: intel_spi_supports_mem_op(struct spi_mem * mem,const struct spi_mem_op * op)
- Line: 757

### intel_spi_sw_cycle
- Return type: static int
- Signature: intel_spi_sw_cycle(struct intel_spi * ispi,u8 opcode,size_t len,int optype)
- Line: 396

### intel_spi_wait_hw_busy
- Return type: static int
- Signature: intel_spi_wait_hw_busy(struct intel_spi * ispi)
- Line: 319

### intel_spi_wait_sw_busy
- Return type: static int
- Signature: intel_spi_wait_sw_busy(struct intel_spi * ispi)
- Line: 328

### intel_spi_write
- Return type: static int
- Signature: intel_spi_write(struct intel_spi * ispi,const struct spi_mem * mem,const struct intel_spi_mem_op * iop,const struct spi_mem_op * op)
- Line: 612

### intel_spi_write_block
- Return type: static int
- Signature: intel_spi_write_block(struct intel_spi * ispi,const void * buf,size_t size)
- Line: 299

### intel_spi_write_reg
- Return type: static int
- Signature: intel_spi_write_reg(struct intel_spi * ispi,const struct spi_mem * mem,const struct intel_spi_mem_op * iop,const struct spi_mem_op * op)
- Line: 490

## Structs (2)

### intel_spi
- Line: 161
- Members:
  - dev: device *
  - info: const struct intel_spi_boardinfo *
  - base: void __iomem *
  - pregs: void __iomem *
  - sregs: void __iomem *
  - host: spi_controller *
  - nregions: size_t
  - pr_num: size_t
  - chip0_size: size_t
  - locked: bool
  - protected: bool
  - bios_locked: bool
  - swseq_reg: bool
  - swseq_erase: bool
  - atomic_preopcode: u8
  - opcodes: u8[8]
  - mem_ops: const struct intel_spi_mem_op *
  - mem_op: spi_mem_op
  - replacement_op: u32
  - exec_op: int (*)(struct intel_spi * ispi,const struct spi_mem * mem,const struct intel_spi_mem_op * iop,const struct spi_mem_op * op)

### intel_spi_mem_op
- Line: 181
- Members:
  - dev: device *
  - info: const struct intel_spi_boardinfo *
  - base: void __iomem *
  - pregs: void __iomem *
  - sregs: void __iomem *
  - host: spi_controller *
  - nregions: size_t
  - pr_num: size_t
  - chip0_size: size_t
  - locked: bool
  - protected: bool
  - bios_locked: bool
  - swseq_reg: bool
  - swseq_erase: bool
  - atomic_preopcode: u8
  - opcodes: u8[8]
  - mem_ops: const struct intel_spi_mem_op *
  - mem_op: spi_mem_op
  - replacement_op: u32
  - exec_op: int (*)(struct intel_spi * ispi,const struct spi_mem * mem,const struct intel_spi_mem_op * iop,const struct spi_mem_op * op)

## Variables (8)

- static **erase_64k_mem_ops** : const struct intel_spi_mem_op[] (line 1058)
- static **generic_mem_ops** : const struct intel_spi_mem_op[] (line 1053)
- static **ignore_protection_status** : bool (line 193)
- static **intel_spi_attr_group** : const struct attribute_group (line 1470)
- static **intel_spi_attrs** : attribute * [] (line 1463)
- **intel_spi_groups** : const struct attribute_group * [] (line 1474)
- static **intel_spi_mem_ops** : const struct spi_controller_mem_ops (line 858)
- static **writeable** : bool (line 190)

## Macros (101)

- **BFPREG** (line 22)
- **BXT_FREG_NUM** (line 106)
- **BXT_PR** (line 104)
- **BXT_PR_NUM** (line 107)
- **BXT_SSFSTS_CTL** (line 105)
- **BYT_FREG_NUM** (line 96)
- **BYT_PR** (line 94)
- **BYT_PR_NUM** (line 97)
- **BYT_SSFSTS_CTL** (line 95)
- **CNL_FREG_NUM** (line 110)
- **CNL_PR** (line 109)
- **CNL_PR_NUM** (line 111)
- **DLOCK** (line 50)
- **ERASE_64K_OPCODE_MASK** (line 118)
- **ERASE_64K_OPCODE_SHIFT** (line 117)
- **ERASE_OPCODE_MASK** (line 116)
- **ERASE_OPCODE_SHIFT** (line 115)
- **FADDR** (line 49)
- **FDATA**(n) (line 51)
- **FLCOMP_C0DEN_128M** (line 135)
- **FLCOMP_C0DEN_16M** (line 132)
- **FLCOMP_C0DEN_1M** (line 128)
- **FLCOMP_C0DEN_2M** (line 129)
- **FLCOMP_C0DEN_32M** (line 133)
- **FLCOMP_C0DEN_4M** (line 130)
- **FLCOMP_C0DEN_512K** (line 127)
- **FLCOMP_C0DEN_64M** (line 134)
- **FLCOMP_C0DEN_8M** (line 131)
- **FLCOMP_C0DEN_MASK** (line 126)
- **FLMAP0_FCBA_MASK** (line 124)
- **FLMAP0_NC_MASK** (line 122)
- **FLMAP0_NC_SHIFT** (line 123)
- **FLVALSIG_MAGIC** (line 121)
- **FRACC** (line 53)
- **FREG**(n) (line 55)
- **FREG_BASE_MASK** (line 56)
- **FREG_LIMIT_MASK** (line 58)
- **FREG_LIMIT_SHIFT** (line 57)
- **HSFSTS_CTL** (line 24)
- **HSFSTS_CTL_AEL** (line 45)
- **HSFSTS_CTL_FCERR** (line 46)
- **HSFSTS_CTL_FCYCLE_ERASE** (line 34)
- **HSFSTS_CTL_FCYCLE_ERASE_64K** (line 35)
- **HSFSTS_CTL_FCYCLE_MASK** (line 30)
- **HSFSTS_CTL_FCYCLE_RDID** (line 37)
- **HSFSTS_CTL_FCYCLE_RDSFDP** (line 36)
- **HSFSTS_CTL_FCYCLE_RDSR** (line 39)
- **HSFSTS_CTL_FCYCLE_READ** (line 32)
- **HSFSTS_CTL_FCYCLE_SHIFT** (line 29)
- **HSFSTS_CTL_FCYCLE_WRITE** (line 33)
- **HSFSTS_CTL_FCYCLE_WRSR** (line 38)
- **HSFSTS_CTL_FDBC_MASK** (line 27)
- **HSFSTS_CTL_FDBC_SHIFT** (line 26)
- **HSFSTS_CTL_FDONE** (line 47)
- **HSFSTS_CTL_FDV** (line 43)
- **HSFSTS_CTL_FGO** (line 41)
- **HSFSTS_CTL_FLOCKDN** (line 42)
- **HSFSTS_CTL_FSMIE** (line 25)
- **HSFSTS_CTL_SCIP** (line 44)
- **INTEL_SPI_FIFO_SZ** (line 138)
- **INTEL_SPI_GENERIC_OPS** (line 917)
- **INTEL_SPI_MEM_OP**(__cmd,__addr,__data,__exec_op) (line 890)
- **INTEL_SPI_MEM_OP_REPL**(__cmd,__addr,__data,__exec_op,__repl) (line 900)
- **INTEL_SPI_OP_ADDR**(__nbytes) (line 868)
- **INTEL_SPI_OP_DATA_IN**(__buswidth) (line 878)
- **INTEL_SPI_OP_DATA_OUT**(__buswidth) (line 884)
- **INTEL_SPI_OP_NO_DATA** (line 873)
- **INTEL_SPI_TIMEOUT** (line 137)
- **LPT_FREG_NUM** (line 101)
- **LPT_PR** (line 99)
- **LPT_PR_NUM** (line 102)
- **LPT_SSFSTS_CTL** (line 100)
- **LVSCC** (line 113)
- **OPMENU0** (line 85)
- **OPMENU1** (line 86)
- **OPTYPE_READ_NO_ADDR** (line 88)
- **OPTYPE_READ_WITH_ADDR** (line 90)
- **OPTYPE_WRITE_NO_ADDR** (line 89)
- **OPTYPE_WRITE_WITH_ADDR** (line 91)
- **PR**(n) (line 61)
- **PREOP_OPTYPE** (line 84)
- **PR_BASE_MASK** (line 66)
- **PR_LIMIT_MASK** (line 64)
- **PR_LIMIT_SHIFT** (line 63)
- **PR_RPE** (line 65)
- **PR_WPE** (line 62)
- **SSFSTS_CTL** (line 69)
- **SSFSTS_CTL_ACS** (line 74)
- **SSFSTS_CTL_AEL** (line 79)
- **SSFSTS_CTL_COP_SHIFT** (line 76)
- **SSFSTS_CTL_DBC_SHIFT** (line 72)
- **SSFSTS_CTL_DOFRS** (line 78)
- **SSFSTS_CTL_DS** (line 71)
- **SSFSTS_CTL_FCERR** (line 80)
- **SSFSTS_CTL_FDONE** (line 81)
- **SSFSTS_CTL_FRS** (line 77)
- **SSFSTS_CTL_FSMIE** (line 70)
- **SSFSTS_CTL_SCGO** (line 75)
- **SSFSTS_CTL_SCIP** (line 82)
- **SSFSTS_CTL_SPOP** (line 73)
- **UVSCC** (line 114)
