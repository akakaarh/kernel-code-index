# drivers/mmc/host/cqhci-core.c

Subsystem: drivers/mmc

## Functions (46)

### __cqhci_disable
- Return type: static void
- Signature: __cqhci_disable(struct cqhci_host * cq_host)
- Line: 306

### __cqhci_enable
- Return type: static void
- Signature: __cqhci_enable(struct cqhci_host * cq_host)
- Line: 251

### cqhci_clear_all_tasks
- Return type: static bool
- Signature: cqhci_clear_all_tasks(struct mmc_host * mmc,unsigned int timeout)
- Line: 935

### cqhci_deactivate
- Return type: int
- Signature: cqhci_deactivate(struct mmc_host * mmc)
- Line: 319

### cqhci_disable
- Return type: static void
- Signature: cqhci_disable(struct mmc_host * mmc)
- Line: 402

### cqhci_dma_map
- Return type: static int
- Signature: cqhci_dma_map(struct mmc_host * host,struct mmc_request * mrq)
- Line: 462

### cqhci_dumpregs
- Return type: static void
- Signature: cqhci_dumpregs(struct cqhci_host * cq_host)
- Line: 113

### cqhci_enable
- Return type: static int
- Signature: cqhci_enable(struct mmc_host * mmc,struct mmc_card * card)
- Line: 337

### cqhci_error_flags
- Return type: static unsigned int
- Signature: cqhci_error_flags(int error1,int error2)
- Line: 686

### cqhci_error_from_flags
- Return type: static int
- Signature: cqhci_error_from_flags(unsigned int flags)
- Line: 1013

### cqhci_error_irq
- Return type: static void
- Signature: cqhci_error_irq(struct mmc_host * mmc,u32 status,int cmd_error,int data_error)
- Line: 700

### cqhci_finish_mrq
- Return type: static void
- Signature: cqhci_finish_mrq(struct mmc_host * mmc,unsigned int tag)
- Line: 788

### cqhci_halt
- Return type: static bool
- Signature: cqhci_halt(struct mmc_host * mmc,unsigned int timeout)
- Line: 961

### cqhci_halted
- Return type: static bool
- Signature: cqhci_halted(struct cqhci_host * cq_host)
- Line: 36

### cqhci_host_alloc_tdl
- Return type: static int
- Signature: cqhci_host_alloc_tdl(struct cqhci_host * cq_host)
- Line: 174

### cqhci_init
- Return type: int
- Signature: cqhci_init(struct cqhci_host * cq_host,struct mmc_host * mmc,bool dma64)
- Line: 1179

### cqhci_irq
- Return type: irqreturn_t
- Signature: cqhci_irq(struct mmc_host * mmc,u32 intmask,int cmd_error,int data_error)
- Line: 822

### cqhci_is_idle
- Return type: static bool
- Signature: cqhci_is_idle(struct cqhci_host * cq_host,int * ret)
- Line: 879

### cqhci_off
- Return type: static void
- Signature: cqhci_off(struct mmc_host * mmc)
- Line: 375

### cqhci_pltfm_init
- Return type: cqhci_host *
- Signature: cqhci_pltfm_init(struct platform_device * pdev)
- Line: 1138

### cqhci_post_req
- Return type: static void
- Signature: cqhci_post_req(struct mmc_host * host,struct mmc_request * mrq)
- Line: 586

### cqhci_prep_dcmd_desc
- Return type: static void
- Signature: cqhci_prep_dcmd_desc(struct mmc_host * mmc,struct mmc_request * mrq)
- Line: 542

### cqhci_prep_task_desc
- Return type: static void
- Signature: cqhci_prep_task_desc(struct mmc_request * mrq,struct cqhci_host * cq_host,int tag)
- Line: 427

### cqhci_prep_tran_desc
- Return type: static int
- Signature: cqhci_prep_tran_desc(struct mmc_request * mrq,struct cqhci_host * cq_host,int tag)
- Line: 505

### cqhci_read_ctl
- Return type: static u32
- Signature: cqhci_read_ctl(struct cqhci_host * cq_host)
- Line: 370

### cqhci_recover_mrq
- Return type: static void
- Signature: cqhci_recover_mrq(struct cqhci_host * cq_host,unsigned int tag)
- Line: 1028

### cqhci_recover_mrqs
- Return type: static void
- Signature: cqhci_recover_mrqs(struct cqhci_host * cq_host)
- Line: 1052

### cqhci_recovery_finish
- Return type: static void
- Signature: cqhci_recovery_finish(struct mmc_host * mmc)
- Line: 1070

### cqhci_recovery_needed
- Return type: static void
- Signature: cqhci_recovery_needed(struct mmc_host * mmc,struct mmc_request * mrq,bool notify)
- Line: 672

### cqhci_recovery_start
- Return type: static void
- Signature: cqhci_recovery_start(struct mmc_host * mmc)
- Line: 997

### cqhci_request
- Return type: static int
- Signature: cqhci_request(struct mmc_host * mmc,struct mmc_request * mrq)
- Line: 602

### cqhci_resume
- Return type: int
- Signature: cqhci_resume(struct mmc_host * mmc)
- Line: 330

### cqhci_set_irqs
- Return type: static void
- Signature: cqhci_set_irqs(struct cqhci_host * cq_host,u32 set)
- Line: 102

### cqhci_set_tran_desc
- Return type: void
- Signature: cqhci_set_tran_desc(u8 * desc,dma_addr_t addr,int len,bool end,bool dma64)
- Line: 482

### cqhci_tag
- Return type: static int
- Signature: cqhci_tag(struct mmc_request * mrq)
- Line: 597

### cqhci_tasks_cleared
- Return type: static bool
- Signature: cqhci_tasks_cleared(struct cqhci_host * cq_host)
- Line: 930

### cqhci_timeout
- Return type: static bool
- Signature: cqhci_timeout(struct mmc_host * mmc,struct mmc_request * mrq,bool * recovery_needed)
- Line: 903

### cqhci_ver_major
- Return type: static unsigned int
- Signature: cqhci_ver_major(struct cqhci_host * cq_host)
- Line: 1167

### cqhci_ver_minor
- Return type: static unsigned int
- Signature: cqhci_ver_minor(struct cqhci_host * cq_host)
- Line: 1172

### cqhci_wait_for_idle
- Return type: static int
- Signature: cqhci_wait_for_idle(struct mmc_host * mmc)
- Line: 893

### get_desc
- Return type: static u8 *
- Signature: get_desc(struct cqhci_host * cq_host,u8 tag)
- Line: 41

### get_link_desc
- Return type: static u8 *
- Signature: get_link_desc(struct cqhci_host * cq_host,u8 tag)
- Line: 46

### get_trans_desc
- Return type: static u8 *
- Signature: get_trans_desc(struct cqhci_host * cq_host,u8 tag)
- Line: 65

### get_trans_desc_dma
- Return type: static dma_addr_t
- Signature: get_trans_desc_dma(struct cqhci_host * cq_host,u8 tag)
- Line: 58

### get_trans_desc_offset
- Return type: static size_t
- Signature: get_trans_desc_offset(struct cqhci_host * cq_host,u8 tag)
- Line: 53

### setup_trans_desc
- Return type: static void
- Signature: setup_trans_desc(struct cqhci_host * cq_host,u8 tag)
- Line: 72

## Structs (1)

### cqhci_slot
- Line: 26
- Members:
  - mrq: mmc_request *
  - flags: unsigned int

## Variables (1)

- static **cqhci_cqe_ops** : const struct mmc_cqe_ops (line 1126)

## Macros (13)

- **CQHCI_CLEAR_TIMEOUT** (line 1068)
- **CQHCI_COMPLETED** (line 30)
- **CQHCI_DUMP**(f,x...) (line 110)
- **CQHCI_EXTERNAL_TIMEOUT** (line 29)
- **CQHCI_FINISH_HALT_TIMEOUT** (line 1065)
- **CQHCI_HOST_CRC** (line 31)
- **CQHCI_HOST_OTHER** (line 33)
- **CQHCI_HOST_TIMEOUT** (line 32)
- **CQHCI_OFF_TIMEOUT** (line 368)
- **CQHCI_START_HALT_TIMEOUT** (line 995)
- **DCMD_SLOT** (line 23)
- **DRV_NAME** (line 108)
- **NUM_SLOTS** (line 24)
