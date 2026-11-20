Task: Move-out logic should use active element ID and valid element IDs.
Status: Complete. Hook compares active ID against mailbox element IDs after loading. Both views receive list/loading; conversation view selects message ID for message-level labels. Hook and ConversationView tests passed (17); Mailbox.elements tests passed (12). Git diff check passed.
