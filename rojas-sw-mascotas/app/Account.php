<?php

namespace App;

use Illuminate\Database\Eloquent\Model;

class Account extends Model
{
    protected $table = 'account';
    protected $fillable = ['id', 'email', 'password', 'is_active', 'is_staff', 'is_superuser','api_token'];
    public $timestamps = false;

    public function person()
    {
        return $this->belongsTo('App\Person');
    }
}
