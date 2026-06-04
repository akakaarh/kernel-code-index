# drivers/mmc/host/sdricoh_cs.c

Subsystem: drivers/mmc

## Functions (17)

### sdricoh_blockio
- Return type: static int
- Signature: sdricoh_blockio(struct sdricoh_host * host,int read,u8 * buf,int len)
- Line: 211

### sdricoh_get_ro
- Return type: static int
- Signature: sdricoh_get_ro(struct mmc_host * mmc)
- Line: 356

### sdricoh_init_mmc
- Return type: static int
- Signature: sdricoh_init_mmc(struct pci_dev * pci_dev,struct pcmcia_device * pcmcia_dev)
- Line: 378

### sdricoh_mmc_cmd
- Return type: static int
- Signature: sdricoh_mmc_cmd(struct sdricoh_host * host,struct mmc_command * cmd)
- Line: 150

### sdricoh_pcmcia_detach
- Return type: static void
- Signature: sdricoh_pcmcia_detach(struct pcmcia_device * link)
- Line: 472

### sdricoh_pcmcia_probe
- Return type: static int
- Signature: sdricoh_pcmcia_probe(struct pcmcia_device * pcmcia_dev)
- Line: 449

### sdricoh_pcmcia_resume
- Return type: static int
- Signature: sdricoh_pcmcia_resume(struct pcmcia_device * link)
- Line: 495

### sdricoh_pcmcia_suspend
- Return type: static int
- Signature: sdricoh_pcmcia_suspend(struct pcmcia_device * link)
- Line: 489

### sdricoh_query_status
- Return type: static int
- Signature: sdricoh_query_status(struct sdricoh_host * host,unsigned int wanted)
- Line: 126

### sdricoh_readb
- Return type: static unsigned int
- Signature: sdricoh_readb(struct sdricoh_host * host,unsigned int reg)
- Line: 111

### sdricoh_readl
- Return type: static unsigned int
- Signature: sdricoh_readl(struct sdricoh_host * host,unsigned int reg)
- Line: 88

### sdricoh_request
- Return type: static void
- Signature: sdricoh_request(struct mmc_host * mmc,struct mmc_request * mrq)
- Line: 254

### sdricoh_reset
- Return type: static int
- Signature: sdricoh_reset(struct sdricoh_host * host)
- Line: 192

### sdricoh_set_ios
- Return type: static void
- Signature: sdricoh_set_ios(struct mmc_host * mmc,struct mmc_ios * ios)
- Line: 335

### sdricoh_status_ok
- Return type: static bool
- Signature: sdricoh_status_ok(struct sdricoh_host * host,unsigned int status,unsigned int wanted)
- Line: 119

### sdricoh_writel
- Return type: static void
- Signature: sdricoh_writel(struct sdricoh_host * host,unsigned int reg,unsigned int value)
- Line: 96

### sdricoh_writew
- Return type: static void
- Signature: sdricoh_writew(struct sdricoh_host * host,unsigned int reg,unsigned short value)
- Line: 104

## Structs (1)

### sdricoh_host
- Line: 78
- Members:
  - dev: device *
  - mmc: mmc_host *
  - iobase: unsigned char __iomem *
  - pci_dev: pci_dev *
  - app_cmd: int

## Variables (4)

- static **pcmcia_ids** : const struct pcmcia_device_id[] (line 66)
- static **sdricoh_driver** : pcmcia_driver (line 507)
- static **sdricoh_ops** : const struct mmc_host_ops (line 371)
- static **switchlocked** : unsigned int (line 30)

## Macros (28)

- **DRIVER_NAME** (line 28)
- **R104_VERSION** (line 37)
- **R200_CMD** (line 38)
- **R204_CMD_ARG** (line 39)
- **R208_DATAIO** (line 40)
- **R20C_RESP** (line 41)
- **R21C_STATUS** (line 42)
- **R224_MODE** (line 46)
- **R226_BLOCKSIZE** (line 47)
- **R228_POWER** (line 48)
- **R230_DATA** (line 49)
- **R2E0_INIT** (line 43)
- **R2E4_STATUS_RESP** (line 44)
- **R2F0_RESET** (line 45)
- **SDRICOH_CMD_TIMEOUT_US** (line 62)
- **SDRICOH_DATA_TIMEOUT_US** (line 63)
- **SDRICOH_PCI_REGION** (line 33)
- **SDRICOH_PCI_REGION_SIZE** (line 34)
- **STATUS_BUSY** (line 59)
- **STATUS_CARD_INSERTED** (line 54)
- **STATUS_CARD_LOCKED** (line 55)
- **STATUS_CMD_FINISHED** (line 52)
- **STATUS_CMD_TIMEOUT** (line 56)
- **STATUS_READY_TO_READ** (line 57)
- **STATUS_READY_TO_WRITE** (line 58)
- **STATUS_TRANSFER_FINISHED** (line 53)
- **sdricoh_pcmcia_resume** (line 504)
- **sdricoh_pcmcia_suspend** (line 503)
