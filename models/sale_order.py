# -*- coding: utf-8 -*-
from odoo import models, fields, api
from odoo.exceptions import UserError, AccessError

class SaleOrder(models.Model):
    _inherit = 'sale.order'
    
    # 重新定義 date_order 欄位以移除預設的唯讀限制
    date_order = fields.Datetime(
        string='Order Date', 
        required=True, 
        readonly=False,  # 移除唯讀限制
        index=True, 
        states={}, 
        copy=False, 
        default=fields.Datetime.now,
        help="建立報價單的日期"
    )
    
    @api.model
    def fields_view_get(self, view_id=None, view_type='form', toolbar=False, submenu=False):
        """動態控制欄位屬性"""
        result = super().fields_view_get(view_id=view_id, view_type=view_type, toolbar=toolbar, submenu=submenu)
        
        # 檢查使用者權限
        has_permission = self.env.user.has_group('sale_order_date_edit.group_edit_order_date')
        
        if result.get('fields') and 'date_order' in result['fields']:
            # 根據權限設定欄位屬性
            if has_permission:
                result['fields']['date_order']['readonly'] = False
                result['fields']['date_order']['states'] = {}
            else:
                result['fields']['date_order']['readonly'] = True
                
        return result
    
    def write(self, vals):
        """寫入時的權限檢查"""
        if 'date_order' in vals:
            # 檢查使用者是否有編輯權限
            if not self.env.user.has_group('sale_order_date_edit.group_edit_order_date'):
                raise AccessError('您沒有權限編輯銷售訂單日期。\n請聯繫系統管理員授予「編輯訂單日期」權限。')
            
            # 記錄變更
            for record in self:
                old_date = record.date_order
                new_date = fields.Datetime.to_datetime(vals['date_order'])
                if old_date != new_date:
                    record.message_post(
                        body=f'訂單日期已從 {old_date.strftime("%Y-%m-%d %H:%M:%S")} 更改為 {new_date.strftime("%Y-%m-%d %H:%M:%S")}',
                        message_type='comment'
                    )
                        
        return super().write(vals)
