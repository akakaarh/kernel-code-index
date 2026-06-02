# drivers/i2c/busses/i2c-i801.c

Subsystem: drivers/i2c

## Functions (49)

### bios_signature
- Return type: static __init const void __iomem *
- Signature: bios_signature(const void __iomem * bios)
- Line: 1081

### dmi_check_onboard_device
- Return type: static void
- Signature: dmi_check_onboard_device(u8 type,const char * name,struct i2c_adapter * adap)
- Line: 1121

### dmi_check_onboard_devices
- Return type: static void
- Signature: dmi_check_onboard_devices(const struct dmi_header * dm,void * adap)
- Line: 1145

### i2c_i801_init
- Return type: static int __init
- Signature: i2c_i801_init(struct pci_driver * drv)
- Line: 1757

### i801_access
- Return type: static s32
- Signature: i801_access(struct i2c_adapter * adap,u16 addr,unsigned short flags,char read_write,u8 command,int size,union i2c_smbus_data * data)
- Line: 891

### i801_acpi_io_handler
- Return type: static acpi_status
- Signature: i801_acpi_io_handler(u32 function,acpi_physical_address address,u32 bits,u64 * value,void * handler_context,void * region_context)
- Line: 1461

### i801_acpi_is_smbus_ioport
- Return type: static bool
- Signature: i801_acpi_is_smbus_ioport(const struct i801_priv * priv,acpi_physical_address address)
- Line: 1453

### i801_acpi_probe
- Return type: static int
- Signature: i801_acpi_probe(struct i801_priv * priv)
- Line: 1518

### i801_acpi_probe
- Return type: static int
- Signature: i801_acpi_probe(struct i801_priv * priv)
- Line: 1498

### i801_acpi_remove
- Return type: static void
- Signature: i801_acpi_remove(struct i801_priv * priv)
- Line: 1519

### i801_acpi_remove
- Return type: static void
- Signature: i801_acpi_remove(struct i801_priv * priv)
- Line: 1511

### i801_add_mux
- Return type: static void
- Signature: i801_add_mux(struct i801_priv * priv)
- Line: 1368

### i801_add_mux
- Return type: static void
- Signature: i801_add_mux(struct i801_priv * priv)
- Line: 1305

### i801_add_tco
- Return type: static void
- Signature: i801_add_tco(struct i801_priv * priv)
- Line: 1415

### i801_add_tco_cnl
- Return type: static platform_device *
- Signature: i801_add_tco_cnl(struct pci_dev * pci_dev,struct resource * tco_res)
- Line: 1404

### i801_add_tco_spt
- Return type: static platform_device *
- Signature: i801_add_tco_spt(struct pci_dev * pci_dev,struct resource * tco_res)
- Line: 1373

### i801_block_transaction_by_block
- Return type: static int
- Signature: i801_block_transaction_by_block(struct i801_priv * priv,union i2c_smbus_data * data,char read_write,int command)
- Line: 515

### i801_block_transaction_byte_by_byte
- Return type: static int
- Signature: i801_block_transaction_byte_by_byte(struct i801_priv * priv,union i2c_smbus_data * data,char read_write,int command)
- Line: 672

### i801_check_and_clear_pec_error
- Return type: static int
- Signature: i801_check_and_clear_pec_error(struct i801_priv * priv)
- Line: 394

### i801_check_post
- Return type: static int
- Signature: i801_check_post(struct i801_priv * priv,int status)
- Line: 442

### i801_check_pre
- Return type: static int
- Signature: i801_check_pre(struct i801_priv * priv)
- Line: 412

### i801_del_mux
- Return type: static void
- Signature: i801_del_mux(struct i801_priv * priv)
- Line: 1369

### i801_del_mux
- Return type: static void
- Signature: i801_del_mux(struct i801_priv * priv)
- Line: 1361

### i801_disable_host_notify
- Return type: static void
- Signature: i801_disable_host_notify(struct i801_priv * priv)
- Line: 983

### i801_enable_host_notify
- Return type: static void
- Signature: i801_enable_host_notify(struct i2c_adapter * adapter)
- Line: 964

### i801_func
- Return type: static u32
- Signature: i801_func(struct i2c_adapter * adapter)
- Line: 947

### i801_get_block_len
- Return type: static int
- Signature: i801_get_block_len(struct i801_priv * priv)
- Line: 382

### i801_host_notify_isr
- Return type: static irqreturn_t
- Signature: i801_host_notify_isr(struct i801_priv * priv)
- Line: 596

### i801_i2c_block_transaction
- Return type: static int
- Signature: i801_i2c_block_transaction(struct i801_priv * priv,union i2c_smbus_data * data,u8 addr,u8 hstcmd,char read_write,int command)
- Line: 849

### i801_isr
- Return type: static irqreturn_t
- Signature: i801_isr(int irq,void * dev_id)
- Line: 629

### i801_isr_byte_done
- Return type: static void
- Signature: i801_isr_byte_done(struct i801_priv * priv)
- Line: 563

### i801_notifier_call
- Return type: static int
- Signature: i801_notifier_call(struct notifier_block * nb,unsigned long action,void * data)
- Line: 1287

### i801_probe
- Return type: static int
- Signature: i801_probe(struct pci_dev * dev,const struct pci_device_id * id)
- Line: 1537

### i801_probe_optional_targets
- Return type: static void
- Signature: i801_probe_optional_targets(struct i801_priv * priv)
- Line: 1200

### i801_probe_optional_targets
- Return type: static void
- Signature: i801_probe_optional_targets(struct i801_priv * priv)
- Line: 1174

### i801_remove
- Return type: static void
- Signature: i801_remove(struct pci_dev * dev)
- Line: 1690

### i801_restore_regs
- Return type: static void
- Signature: i801_restore_regs(struct i801_priv * priv)
- Line: 1531

### i801_resume
- Return type: static int
- Signature: i801_resume(struct device * dev)
- Line: 1732

### i801_set_hstadd
- Return type: static void
- Signature: i801_set_hstadd(struct i801_priv * priv,u8 addr,char read_write)
- Line: 757

### i801_setup_hstcfg
- Return type: static void
- Signature: i801_setup_hstcfg(struct i801_priv * priv)
- Line: 1522

### i801_shutdown
- Return type: static void
- Signature: i801_shutdown(struct pci_dev * dev)
- Line: 1713

### i801_simple_transaction
- Return type: static int
- Signature: i801_simple_transaction(struct i801_priv * priv,union i2c_smbus_data * data,u8 addr,u8 hstcmd,char read_write,int command)
- Line: 763

### i801_smbus_block_transaction
- Return type: static int
- Signature: i801_smbus_block_transaction(struct i801_priv * priv,union i2c_smbus_data * data,u8 addr,u8 hstcmd,char read_write,int command)
- Line: 827

### i801_suspend
- Return type: static int
- Signature: i801_suspend(struct device * dev)
- Line: 1722

### i801_transaction
- Return type: static int
- Signature: i801_transaction(struct i801_priv * priv,int xact)
- Line: 497

### i801_wait_byte_done
- Return type: static int
- Signature: i801_wait_byte_done(struct i801_priv * priv)
- Line: 367

### i801_wait_intr
- Return type: static int
- Signature: i801_wait_intr(struct i801_priv * priv)
- Line: 349

### input_apanel_init
- Return type: static void __init
- Signature: input_apanel_init(void)
- Line: 1199

### input_apanel_init
- Return type: static void __init
- Signature: input_apanel_init(void)
- Line: 1094

## Structs (3)

### dmi_onboard_device_info
- Line: 1108
- Members:
  - gpio_chip: char *
  - values: unsigned[3]
  - n_values: int
  - gpios: unsigned[2]
  - n_gpios: int
  - adapter: i2c_adapter
  - smba: void __iomem *
  - original_hstcfg: unsigned char
  - original_hstcnt: unsigned char
  - original_slvcmd: unsigned char
  - pci_dev: pci_dev *
  - features: unsigned int
  - done: completion
  - status: u8
  - cmd: u8
  - is_read: bool
  - count: int
  - len: int
  - data: u8 *
  - mux_pdev: platform_device *
  - lookup: gpiod_lookup_table *
  - mux_notifier_block: notifier_block
  - tco_pdev: platform_device *
  - acpi_reserved: bool
  - acpi_lock: mutex
  - name: const char *
  - type: u8
  - i2c_addr: unsigned short
  - i2c_type: const char *

### i801_mux_config
- Line: 276
- Members:
  - gpio_chip: char *
  - values: unsigned[3]
  - n_values: int
  - gpios: unsigned[2]
  - n_gpios: int
  - adapter: i2c_adapter
  - smba: void __iomem *
  - original_hstcfg: unsigned char
  - original_hstcnt: unsigned char
  - original_slvcmd: unsigned char
  - pci_dev: pci_dev *
  - features: unsigned int
  - done: completion
  - status: u8
  - cmd: u8
  - is_read: bool
  - count: int
  - len: int
  - data: u8 *
  - mux_pdev: platform_device *
  - lookup: gpiod_lookup_table *
  - mux_notifier_block: notifier_block
  - tco_pdev: platform_device *
  - acpi_reserved: bool
  - acpi_lock: mutex
  - name: const char *
  - type: u8
  - i2c_addr: unsigned short
  - i2c_type: const char *

### i801_priv
- Line: 284
- Members:
  - gpio_chip: char *
  - values: unsigned[3]
  - n_values: int
  - gpios: unsigned[2]
  - n_gpios: int
  - adapter: i2c_adapter
  - smba: void __iomem *
  - original_hstcfg: unsigned char
  - original_hstcnt: unsigned char
  - original_slvcmd: unsigned char
  - pci_dev: pci_dev *
  - features: unsigned int
  - done: completion
  - status: u8
  - cmd: u8
  - is_read: bool
  - count: int
  - len: int
  - data: u8 *
  - mux_pdev: platform_device *
  - lookup: gpiod_lookup_table *
  - mux_notifier_block: notifier_block
  - tco_pdev: platform_device *
  - acpi_reserved: bool
  - acpi_lock: mutex
  - name: const char *
  - type: u8
  - i2c_addr: unsigned short
  - i2c_type: const char *

## Variables (10)

- static **__ro_after_init** : unsigned char apanel_addr (line 1078)
- static **disable_features** : unsigned int (line 339)
- static **dmi_devices** : const struct dmi_onboard_device_info[] (line 1115)
- static **i801_driver** : pci_driver (line 1745)
- static **i801_feature_names** : const char * [] (line 330)
- static **i801_ids** : const struct pci_device_id[] (line 1001)
- static **i801_mux_config_asus_z8_d12** : i801_mux_config (line 1204)
- static **i801_mux_config_asus_z8_d18** : i801_mux_config (line 1212)
- static **mux_dmi_table** : const struct dmi_system_id[] (line 1220)
- static **smbus_algorithm** : const struct i2c_algorithm (line 991)

## Macros (123)

- **DRV_NAME** (line 103)
- **FEATURES_ICH4** (line 996)
- **FEATURES_ICH5** (line 998)
- **FEATURE_BLOCK_BUFFER** (line 320)
- **FEATURE_BLOCK_PROC** (line 321)
- **FEATURE_HOST_NOTIFY** (line 324)
- **FEATURE_I2C_BLOCK_READ** (line 322)
- **FEATURE_IDF** (line 326)
- **FEATURE_IRQ** (line 323)
- **FEATURE_SMBUS_PEC** (line 319)
- **FEATURE_TCO_CNL** (line 328)
- **FEATURE_TCO_SPT** (line 327)
- **I801_BLOCK_DATA** (line 182)
- **I801_BLOCK_PROC_CALL** (line 184)
- **I801_BYTE** (line 178)
- **I801_BYTE_DATA** (line 179)
- **I801_I2C_BLOCK_DATA** (line 183)
- **I801_PROC_CALL** (line 181)
- **I801_QUICK** (line 177)
- **I801_WORD_DATA** (line 180)
- **PCI_DEVICE_ID_INTEL_5_3400_SERIES_SMBUS** (line 239)
- **PCI_DEVICE_ID_INTEL_ALDER_LAKE_M_SMBUS** (line 245)
- **PCI_DEVICE_ID_INTEL_ALDER_LAKE_P_SMBUS** (line 244)
- **PCI_DEVICE_ID_INTEL_ALDER_LAKE_S_SMBUS** (line 252)
- **PCI_DEVICE_ID_INTEL_ARROW_LAKE_H_SMBUS** (line 250)
- **PCI_DEVICE_ID_INTEL_AVOTON_SMBUS** (line 232)
- **PCI_DEVICE_ID_INTEL_BAYTRAIL_SMBUS** (line 221)
- **PCI_DEVICE_ID_INTEL_BIRCH_STREAM_SMBUS** (line 246)
- **PCI_DEVICE_ID_INTEL_BRASWELL_SMBUS** (line 233)
- **PCI_DEVICE_ID_INTEL_BROXTON_SMBUS** (line 248)
- **PCI_DEVICE_ID_INTEL_CANNONLAKE_H_SMBUS** (line 270)
- **PCI_DEVICE_ID_INTEL_CANNONLAKE_LP_SMBUS** (line 264)
- **PCI_DEVICE_ID_INTEL_CDF_SMBUS** (line 222)
- **PCI_DEVICE_ID_INTEL_COLETOCREEK_SMBUS** (line 235)
- **PCI_DEVICE_ID_INTEL_COMETLAKE_H_SMBUS** (line 220)
- **PCI_DEVICE_ID_INTEL_COMETLAKE_SMBUS** (line 219)
- **PCI_DEVICE_ID_INTEL_COMETLAKE_V_SMBUS** (line 271)
- **PCI_DEVICE_ID_INTEL_COUGARPOINT_SMBUS** (line 225)
- **PCI_DEVICE_ID_INTEL_DH89XXCC_SMBUS** (line 234)
- **PCI_DEVICE_ID_INTEL_DIAMOND_RAPIDS_SMBUS** (line 247)
- **PCI_DEVICE_ID_INTEL_DNV_SMBUS** (line 223)
- **PCI_DEVICE_ID_INTEL_EBG_SMBUS** (line 224)
- **PCI_DEVICE_ID_INTEL_ELKHART_LAKE_SMBUS** (line 241)
- **PCI_DEVICE_ID_INTEL_GEMINILAKE_SMBUS** (line 236)
- **PCI_DEVICE_ID_INTEL_ICELAKE_LP_SMBUS** (line 237)
- **PCI_DEVICE_ID_INTEL_ICELAKE_N_SMBUS** (line 238)
- **PCI_DEVICE_ID_INTEL_JASPER_LAKE_SMBUS** (line 243)
- **PCI_DEVICE_ID_INTEL_KABYLAKE_PCH_H_SMBUS** (line 269)
- **PCI_DEVICE_ID_INTEL_LEWISBURG_SMBUS** (line 267)
- **PCI_DEVICE_ID_INTEL_LEWISBURG_SSKU_SMBUS** (line 268)
- **PCI_DEVICE_ID_INTEL_LYNXPOINT_LP_SMBUS** (line 261)
- **PCI_DEVICE_ID_INTEL_LYNXPOINT_SMBUS** (line 255)
- **PCI_DEVICE_ID_INTEL_METEOR_LAKE_PCH_S_SMBUS** (line 254)
- **PCI_DEVICE_ID_INTEL_METEOR_LAKE_P_SMBUS** (line 253)
- **PCI_DEVICE_ID_INTEL_METEOR_LAKE_SOC_S_SMBUS** (line 272)
- **PCI_DEVICE_ID_INTEL_NOVA_LAKE_S_SMBUS** (line 249)
- **PCI_DEVICE_ID_INTEL_PANTHERPOINT_SMBUS** (line 231)
- **PCI_DEVICE_ID_INTEL_PANTHER_LAKE_H_SMBUS** (line 273)
- **PCI_DEVICE_ID_INTEL_PANTHER_LAKE_P_SMBUS** (line 274)
- **PCI_DEVICE_ID_INTEL_PATSBURG_SMBUS** (line 226)
- **PCI_DEVICE_ID_INTEL_PATSBURG_SMBUS_IDF0** (line 228)
- **PCI_DEVICE_ID_INTEL_PATSBURG_SMBUS_IDF1** (line 229)
- **PCI_DEVICE_ID_INTEL_PATSBURG_SMBUS_IDF2** (line 230)
- **PCI_DEVICE_ID_INTEL_RAPTOR_LAKE_S_SMBUS** (line 251)
- **PCI_DEVICE_ID_INTEL_SUNRISEPOINT_H_SMBUS** (line 266)
- **PCI_DEVICE_ID_INTEL_SUNRISEPOINT_LP_SMBUS** (line 263)
- **PCI_DEVICE_ID_INTEL_TIGERLAKE_H_SMBUS** (line 240)
- **PCI_DEVICE_ID_INTEL_TIGERLAKE_LP_SMBUS** (line 265)
- **PCI_DEVICE_ID_INTEL_WELLSBURG_SMBUS** (line 257)
- **PCI_DEVICE_ID_INTEL_WELLSBURG_SMBUS_MS0** (line 258)
- **PCI_DEVICE_ID_INTEL_WELLSBURG_SMBUS_MS1** (line 259)
- **PCI_DEVICE_ID_INTEL_WELLSBURG_SMBUS_MS2** (line 260)
- **PCI_DEVICE_ID_INTEL_WILDCATPOINT_LP_SMBUS** (line 262)
- **PCI_DEVICE_ID_INTEL_WILDCATPOINT_SMBUS** (line 256)
- **PCI_DEVICE_ID_INTEL_WILDCAT_LAKE_U_SMBUS** (line 242)
- **SBREG_SMBCTRL** (line 156)
- **SBREG_SMBCTRL_DNV** (line 157)
- **SMBAUXCTL**(p) (line 144)
- **SMBAUXCTL_CRC** (line 173)
- **SMBAUXCTL_E32B** (line 174)
- **SMBAUXSTS**(p) (line 143)
- **SMBAUXSTS_CRCE** (line 169)
- **SMBAUXSTS_STCO** (line 170)
- **SMBBAR** (line 151)
- **SMBBAR_MMIO** (line 150)
- **SMBBLKDAT**(p) (line 141)
- **SMBHSTADD**(p) (line 138)
- **SMBHSTCFG** (line 152)
- **SMBHSTCFG_HST_EN** (line 160)
- **SMBHSTCFG_I2C_EN** (line 162)
- **SMBHSTCFG_SMB_SMI_EN** (line 161)
- **SMBHSTCFG_SPD_WD** (line 163)
- **SMBHSTCMD**(p) (line 137)
- **SMBHSTCNT**(p) (line 136)
- **SMBHSTCNT_INTREN** (line 187)
- **SMBHSTCNT_KILL** (line 188)
- **SMBHSTCNT_LAST_BYTE** (line 189)
- **SMBHSTCNT_PEC_EN** (line 191)
- **SMBHSTCNT_START** (line 190)
- **SMBHSTDAT0**(p) (line 139)
- **SMBHSTDAT1**(p) (line 140)
- **SMBHSTSTS**(p) (line 135)
- **SMBHSTSTS_BUS_ERR** (line 198)
- **SMBHSTSTS_BYTE_DONE** (line 194)
- **SMBHSTSTS_DEV_ERR** (line 199)
- **SMBHSTSTS_FAILED** (line 197)
- **SMBHSTSTS_HOST_BUSY** (line 201)
- **SMBHSTSTS_INTR** (line 200)
- **SMBHSTSTS_INUSE_STS** (line 195)
- **SMBHSTSTS_SMBALERT_STS** (line 196)
- **SMBNTFDADD**(p) (line 147)
- **SMBPEC**(p) (line 142)
- **SMBSLVCMD**(p) (line 146)
- **SMBSLVCMD_HST_NTFY_INTREN** (line 208)
- **SMBSLVCMD_SMBALERT_DISABLE** (line 207)
- **SMBSLVSTS**(p) (line 145)
- **SMBSLVSTS_HST_NTFY_STS** (line 204)
- **SMBUS_LEN_SENTINEL** (line 216)
- **STATUS_ERROR_FLAGS** (line 210)
- **STATUS_FLAGS** (line 213)
- **TCOBASE** (line 153)
- **TCOCTL** (line 154)
- **TCOCTL_EN** (line 166)
