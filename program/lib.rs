use anchor_lang::prelude::*;


declare_id!("GXV2cYjG8ECRermN9f6X2zpsQsRqF34BEMNjGWGEqkCi");

#[program]
mod hello_anchor {
    use super::*;
    pub fn initialize(ctx: Context<Initialize>, data: u64) -> Result<()> {
        ctx.accounts.new_account.data = data;
        msg!("Changed data to: {}!", data); 
        Ok(())
    }

    pub fn modify_data(ctx: Context<ModifyData>, data: u64) -> Result<u64> {
        ctx.accounts.new_account.data = data;
        msg!("Modified data to: {}!", data);
        Ok(data)
    }

    pub fn read_data(ctx: Context<ReadData>) -> Result<u64> {
        Ok(ctx.accounts.new_account.data)
    }
}

#[derive(Accounts)]
pub struct Initialize<'info> {
    // We must specify the space in order to initialize an account.
    // First 8 bytes are default account discriminator,
    // next 8 bytes come from NewAccount.data being type u64.
    // (u64 = 64 bits unsigned integer = 8 bytes)
    #[account(init, payer = signer, space = 8 + 8)]
    pub new_account: Account<'info, NewAccount>,
    #[account(mut)]
    pub signer: Signer<'info>,
    pub system_program: Program<'info, System>,
}

#[derive(Accounts)]
pub struct ModifyData<'info> {
    #[account(mut)]
    pub new_account: Account<'info, NewAccount>,
}

#[derive(Accounts)]
pub struct ReadData<'info> {
    pub new_account: Account<'info, NewAccount>,
}

#[account]
pub struct NewAccount {
    data: u64,
}
