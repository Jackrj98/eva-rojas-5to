<?php

namespace App;

use Illuminate\Database\Eloquent\Model;

class Role extends Model
{
    protected $table = 'role';
    protected $fillable = ['id', 'name', 'status'];
    public $timestamps = false;

    public function person()
    {
        return $this->hasMany('App\Person');
    }
}
